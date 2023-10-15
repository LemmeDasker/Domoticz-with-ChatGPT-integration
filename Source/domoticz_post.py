#############################################################################################################
#                    FUNCTION:
# Get's the device names passed and the action needed.
# Send the IDX and the required status to Domoticz's API.
#
#                   Your job:
# Apply your own username/password for Domoticz.
# Identify your own devices IDX in Domotic.
# Identify the action you want for the device. Could be On/Off or Open/Closed etc.
#############################################################################################################

import requests
import base64

def http_post(lamp, action):
# Apply your own username/password for Domoticz.
    username = 'YOUR-USERNAME'
    password = 'YOUR-PASSWORD'

# Identify your own devices IDX in Domotic.
    if lamp == 'spisebordslampe': lamp = 36    
    if lamp == 'bordlampe': lamp = 25
    if lamp == 'standerlampe': lamp = 56   
    if lamp == 'gulvlampe': lamp = 92

# Identify the action you want for the device. Could be On/Off or Open/Closed etc.
    if action == 'tænd': action = 'On'
    if action == 'sluk': action = 'Off'

    url = f'https://YOUR.OWN.DOMAIN/json.htm?type=command&param=switchlight&idx={lamp}&switchcmd={action}'

    headers = {
        'Authorization': f'Basic {base64.b64encode(f"{username}:{password}".encode()).decode()}'
    }
    try:
        response = requests.post(url, headers=headers, verify=False)  # Set verify=False to ignore SSL certificate validation
    except Exception as e:
        print(f"An error occurred: {str(e)}")
