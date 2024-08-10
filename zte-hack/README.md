# ZTE F660 Hack

Some ISPs automatically push WAN config to their ONTs using GPON OMCI. This autoconfig creates a config and prevents these from being used with an external router/firewall like a Unifi gateway or Pfsense. This script is a hack to delete the auto configured PPPoE interface everytime the router is restarted. Only works with the ZTE F660.
