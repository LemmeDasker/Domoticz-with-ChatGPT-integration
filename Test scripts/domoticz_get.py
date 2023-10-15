#############################################################################################################
#                    FUNCTION:
# Get's the full status of all devices from Domoticz's API.
# Prints the JSON response.
#
#                   Your job:
# Define your Domoticz username and password
# Change the URL to point to your local Domoticz
#############################################################################################################

import requests
import base64
import json

def http_get():

# Define your Domoticz username and password
    username = 'YOUR-USERNAME'
    password = 'YOUR-PASSWORD'

# Change the URL to point to your local Domoticz
    url = 'https://YOUR.OWN.DOMAIN/json.htm?type=command&param=getdevices&filter=all&used=true&order=Name'
    headers = {
        'Authorization': f'Basic {base64.b64encode(f"{username}:{password}".encode()).decode()}'
    }
    try:
        response = requests.get(url, headers=headers, verify=False)  # Set verify=False to ignore SSL certificate validation
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    data = json.loads(response.text)
    print(data)

http_get()
