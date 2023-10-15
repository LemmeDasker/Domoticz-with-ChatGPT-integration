#############################################################################################################
#                    FUNCTION:
# Get's the full status of all devices from Domoticz's API.
# As this is based on a Danish speaking example, the character 'Ø' needs to be restored in the text. Not needed for UK language. 
# Extract only information about the doors (open/closed), and send it to ChatGPT as part of the conversation.
#
#                   Your job:
# Apply your own username/password for Domoticz.
# Identify your own devices in Domoticz you want to report on.
#############################################################################################################

import requests
import base64
import json

def http_get():
# Apply your own username/password for Domoticz.
    username = 'YOUR-USERNAME'
    password = 'YOUR-PASSWORD'

    url = 'https://YOUR.OWN.DOMAIN/json.htm?type=command&param=getdevices&filter=all&used=true&order=Name'

    headers = {
        'Authorization': f'Basic {base64.b64encode(f"{username}:{password}".encode()).decode()}'
    }
    try:
        response = requests.get(url, headers=headers, verify=False)  # Set verify=False to ignore SSL certificate validation
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    data = json.loads(response.text)

    # Opret et tomt JSON-objekt til at holde det nye data
    result_json = {}

    # Gå igennem hver enhed i den originale JSON og opdater værdien "Havedør\u00f8r"
    for item in data["result"]:
        device_name = item["Name"].replace("\u00f8", "ø")
        # Erstat "Havedør\u00f8r" med "Havedør" i nøglerne
        device_name = device_name.replace("Havedørø", "Havedør")
# Identify your own devices in Domoticz you want to report on.
        if device_name in ["Havedør", "Hoveddør", "Skur"]:
            result_json[device_name] = item["Data"]

    # Konverter result_json til en JSON-streng
    output_json_str = json.dumps(result_json, indent=4, ensure_ascii=False)

    # Udskriv den ønskede JSON-streng
    #print(output_json_str)
    return output_json_str
