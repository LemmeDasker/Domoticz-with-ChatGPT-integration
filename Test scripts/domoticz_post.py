#############################################################################################################
#                    FUNCTION:
# Toggles a device On/Off using the device IDX.
# Send the IDX together with the Toggle command to Domoticz's API.
#
#                   Your job:
# Apply your own username/password for Domoticz.
# Identify your own devices IDX in Domoticz.
# Change the URL to point to your local Domoticz.
#############################################################################################################

import requests
import base64

def http_post():

# Define your Domoticz username/password and the idx for the switch you want to toggle
    username = 'YOUR-USERNAME'
    password = 'YOUR-PASSWORD'
    idx = 36 # Change to your specific IDX number 

# Change the URL to point to your local Domoticz
    url = f'https://YOUR.OWN.DOMAIN/json.htm?type=command&param=switchlight&idx={idx}&switchcmd=Toggle'
    headers = {
        'Authorization': f'Basic {base64.b64encode(f"{username}:{password}".encode()).decode()}'
    }
    try:
        response = requests.post(url, headers=headers, verify=False)  # Set verify=False to ignore SSL certificate validation
    except Exception as e:
        print(f"An error occurred: {str(e)}")

http_post()