# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

#############################################################################################################
#                    FUNCTION:
# Send a text to Azure's Text-to-Speach service.
# Play the voice on the speaker. 
#
#                   Your job:
# Choose the text you want to send.
# Replace with your own subscription key and service region (e.g., "westus").
# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
#############################################################################################################

import azure.cognitiveservices.speech as speechsdk

def speak():
# Choose the text you want to send.
    text = "Hello - I am your new best friend"

    # Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
    speech_key, service_region = "<Your-SUBSCRIPTION-KEY>", "<Your-REGION>"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
    speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"

    # Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    # The synthesized speech is expected to be heard on the speaker with this line executed.
    result = speech_synthesizer.speak_text_async(text).get()

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized to speaker for text [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")

speak()