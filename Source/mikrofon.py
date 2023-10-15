# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

#############################################################################################################
#                    FUNCTION:
# Send the speach from the microphone to Azure's Speach-to-Text.
# Returnes the text to ChatGPT as it's instructions. 
#
#                   Your job:
# Replace with your own subscription key and service region (e.g., "westus").
# Set the language that needs to be processed.
#############################################################################################################

import azure.cognitiveservices.speech as speechsdk

def recognize_from_microphone():
# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
    speech_key, service_region = "<Your-SUBSCRIPTION-KEY>", "<Your-REGION>"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
# Set the language that needs to be processed.
    speech_config.speech_recognition_language="da-DK"

# Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    #print("Sig noget...")

# Starts speech recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
# seconds of audio is processed.  The task returns the recognition text as result. 
# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# shot recognition like command or query. 
# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    result = speech_recognizer.recognize_once()
    return(result.text)
