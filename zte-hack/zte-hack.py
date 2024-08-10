import logging, os, re, requests
from ping3 import ping
from time import sleep

INTERNET_CHECK_IP = os.getenv("INTERNET_CHECK_IP", "1.1.1.1")
INTERNET_CHECK_ALT_IP = os.getenv("INTERNET_CHECK_ALT_IP", "8.8.8.8")
INTERVAL_SECONDS = int(os.getenv("INTERVAL_SECONDS", "10"))

ROUTER_IP = os.getenv("ROUTER_IP", "192.168.8.1")
ROUTER_URL = os.getenv("ROUTER_URL", f"http://{ROUTER_IP}")
ROUTER_USERNAME = os.getenv("ROUTER_USERNAME", "admin")
ROUTER_PASSWORD = os.getenv("ROUTER_PASSWORD", "admin")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(level=LOG_LEVEL)


def delete_wan_from_ont():
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

    response = s.post(
        ROUTER_URL,
        allow_redirects=False,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=data,
    )
    response = s.get(f"{ROUTER_URL}/start.ghtml")

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
    return response


if __name__ == "__main__":
    LAST_ONLINE = False
    while True:
        if ping(INTERNET_CHECK_IP) or ping(INTERNET_CHECK_ALT_IP):
            if not LAST_ONLINE:
                logging.info(
                    f"Looks like internet is reachable. Sleeping for {INTERVAL_SECONDS} seconds"
                )
            LAST_ONLINE = True
            sleep(INTERVAL_SECONDS)
        else:
            logging.info(
                "Looks like internet is unreachable. Checking if CPE is reachable"
            )
            LAST_ONLINE = False
            if ping(ROUTER_IP):
                logging.info("CPE is reachable. Deleting WAN interface")
                delete_wan_from_ont()
            else:
                logging.info("CPE is also unreachable. Trying again")
