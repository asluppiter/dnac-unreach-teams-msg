# dnac-unreach-teams-msg
The python scripts connects and generates a token to the Cisco DNA Controller, in order to get the list of devices and if a device its marked as unreachable or partial collection failure the script will get more information about the device and send it into a MS Teams channel via WebHook

#Installing
Run the bash installer script for dependencies, it will also ask you for the credentials for your DNA account, the FQDN o IP address of your DNA instance and the URL of your incoming WebHook for the notifications on a channel in MS Teams and the given values will replace the placeholders (REMPLAZO_XYZ) on the Python Script.

