# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

#############################################################################################################
#                    FUNCTION:
# Starts the ChatGPT session.
# Get's the status of the doors in the house from Domoticz. The status is sent to ChatGPT as part of the conversation.
# A welcome voice is played indicating that it is ready for listening for commands.  
# Use microphone with Azure Voice-to-Text and use response as input to ChatGPT. 
# Sent text together with example response to learn ChatGPT how to response in desired format.  
# Check if response is a valid JSON. If so, extract the key/value (commands) and send them to Domoticz
# If it is no a valid JSON, it is a normal text response that are passed to Azure's Text-to-Voice. 
#
#                   Your job:
# Change the welcome voice to your liking.
# Create your own example responses based on what you want Domoticz to control.
# Create your own 'system' promp to get ChatGPT to understand what you want it to do.
# Load your API key from an environment variable or secret management service
#############################################################################################################

import lyd
import mikrofon
import openai
import domoticz_post
import domoticz_get
import json


def start():
    output_json = domoticz_get.http_get()
    #print(output_json)   

# Change the welcome voice to your liking.
    lyd.speak_danish("Ja, hvad kan jeg hjælpe med")    

    result = mikrofon.recognize_from_microphone()
    #print(result)

# Create your own example responses based on what you want Domoticz to control.
    example_response = "{\"spisebordslampe\": \"sluk\", \"standerlampe\": \"sluk\", \"gulvlampe\": \"sluk\", \"bordlampe\": \"sluk\"}"

    #result = "kan du slukke alt lyset"
    #result = "kan du tænde lampen der hænger over spisebordet"
    #result = "hvor langt er der fra jorden til månen"
    #result = "kan du se om hoveddøren er åben"

# Create your own 'system' promp to get ChatGPT to understand what you want it to do.
    messages=[
                    {"role": "system", "content": f"Du er primært et Home Automation System der analyserer komplekse instruktioner men du kan også være en Digital Assistent der giver korte svar. I huset er der fire lamper eller lys: spisebordslampe, standerlampe, gulvlampe, bordlampe og de kan have værdierne: tænd, sluk. Instruktionerne er at tænde eller slukke lamper eller lys i huset og du skal vurdere hvilke lamper eller lys der skal tændes eller slukkes og kun svare i JSON:{example_response}. Du skal også kunne give en status på de døre der spørges til. Her er den aktuelle status på alle dørene: {output_json}, men du skal svare med dine egne ord og kun give svar på de døre der bliver spurgt til"},
                    {"role": "user", "content": "Gider du slukke lyset"},
                    {"role": "assistant", "content": f"{example_response}"},
                    {"role": "user", "content": result}
    ]


    if result != "":
    # Load your API key from an environment variable or secret management service
            openai.api_key = "<Your-API-KEY>"

            chat_completion = openai.ChatCompletion.create(
                model="gpt-4-0613",
                #model="gpt-3.5-turbo-0613",
                messages=messages,
            )
            print(chat_completion)

            json_text = chat_completion['choices'][0]['message']['content']
            #print(json_text)

            def load_json(text):
                try:
                    data = json.loads(text)
                    return data
                except json.JSONDecodeError as e:
                    print(f"Fejl: Ugyldig JSON-streng - {e}")
                    return None

            # Prøv at indlæse JSON-data fra strengen
            json_data = load_json(json_text)

            # Tjek om indlæsningen var succesfuld
            if json_data is not None:
                data = json.loads(json_text)
                for key, value in data.items():
                    #print("Nøgle: ", key)
                    #print("Værdi: ", value)
                    domoticz_post.http_post(key, value)
            else:
                #print("Kunne ikke indlæse JSON-data.")
                lyd.speak_danish(json_text)
