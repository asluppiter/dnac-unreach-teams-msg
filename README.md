# dnac-unreach-teams-msg
The python scripts connects and generates a token to the Cisco DNA Controller with an API Call, in order to get the list of devices  (with another API Call) and if a device its marked as unreachable or partial collection failure the script will get more information about the device and send it into a MS Teams channel via WebHook

# Installing
Run the bash installer script for dependencies, it will also ask you for the credentials for your DNA account, the FQDN o IP address of your DNA instance and the URL of your incoming WebHook for the notifications on a channel in MS Teams and the given values will replace the placeholders (REMPLAZO_XYZ) on the Python Script and it will rename it to unreach_Mssg.py

## Example

![Image](https://i.imgur.com/Vzl0485.png)

