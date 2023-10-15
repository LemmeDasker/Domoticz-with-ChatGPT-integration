# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

#############################################################################################################
#                    FUNCTION:
# Get's the text response from ChatGPT and send it to Azure's Text-to-Speach service.
#
#                   Your job:
# Replace with your own subscription key and service region (e.g., "westus").
# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
#############################################################################################################

import azure.cognitiveservices.speech as speechsdk

def speak_danish(text):
# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
    speech_key, service_region = "<Your-SUBSCRIPTION-KEY>", "<Your-REGION>"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
    speech_config.speech_synthesis_voice_name = "da-DK-ChristelNeural"

# Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# The synthesized speech is expected to be heard on the speaker with this line executed.
    result = speech_synthesizer.speak_text_async(text).get()
