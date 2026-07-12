import html, logging, os, re, requests
from time import sleep

INTERVAL_SECONDS = int(os.getenv("INTERVAL_SECONDS", "300"))

ROUTER_IP = os.getenv("ROUTER_IP", "192.168.8.1")
ROUTER_URL = os.getenv("ROUTER_URL", f"http://{ROUTER_IP}")
ROUTER_USERNAME = os.getenv("ROUTER_USERNAME", "admin")
ROUTER_PASSWORD = os.getenv("ROUTER_PASSWORD", "admin")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(level=LOG_LEVEL)


class SessionLoggedOut(Exception):
    pass


def login():
    s = requests.Session()

    response = s.get(ROUTER_URL)
    login_token = re.search('Frm_Logintoken.*"([0-9][0-9]*?)"', response.text).group(1)

    data = {
        "frashnum": "",
        "action": "login",
        "Frm_Logintoken": login_token,
        "Username": ROUTER_USERNAME,
        "Password": ROUTER_PASSWORD,
    }

    s.post(
        ROUTER_URL,
        allow_redirects=False,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=data,
    )
    s.get(f"{ROUTER_URL}/start.ghtml")

    return s


def check_wan(s):
    params = {
        "pid": "1002",
        "nextpage": "IPv46_status_wan2_if_t.gch",
    }
    response = s.get(f"{ROUTER_URL}/getpage.gch", params=params)

    if "logout_redirect" in response.text:
        raise SessionLoggedOut

    return "omci_ipv4_pppoe_1" in html.unescape(response.text)


def delete_wan(s):
    params = {
        "pid": "1002",
        "nextpage": "IPv46_net_wan2_conf_t.gch",
    }
    response = s.post(f"{ROUTER_URL}/getpage.gch", params=params)
    session_token = re.search('session_token.*"([0-9][0-9]*?)"', response.text).group(1)

    data = {
        "IF_ACTION": "delete",
        "IF_ERRORSTR": "SUCC",
        "IF_ERRORPARAM": "SUCC",
        "IF_ERRORTYPE=": "1",
        "IF_Uplink": "2",
        "IF_WANCTYPE": "pppoe",
        "Enable": "1",
        "WANCName": "omci_ipv4_pppoe_1",
        "ConnType": "IP_Routed",
        "StrServList": "INTERNET_VoIP_TR069",
        "ServList": "7",
        "IF_IDENTITY": "IGD.WD1.WCD1.WCPPP5",
        "IF_TYPE": "NULL",
        "IF_INSTNUM": "3",
        "_SESSION_TOKEN": session_token,
    }
    response = s.post(
        f"{ROUTER_URL}/getpage.gch",
        params=params,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=data,
    )
    logging.info("Deleted omci_ipv4_pppoe_1 WAN interface")
    return response


if __name__ == "__main__":
    s = None
    while True:
        try:
            if s is None:
                s = login()

            exists = check_wan(s)

            if exists:
                delete_wan(s)
            else:
                logging.debug("omci_ipv4_pppoe_1 WAN interface not found. Nothing to delete")
        except SessionLoggedOut:
            logging.info("Session logged out. Logging in again next iteration")
            s.close()
            s = None
        except requests.exceptions.RequestException:
            logging.info("CPE is unreachable. Trying again")
            s = None

        sleep(INTERVAL_SECONDS)
