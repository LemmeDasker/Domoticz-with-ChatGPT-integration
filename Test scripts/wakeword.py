#############################################################################################################
#                    FUNCTION:
# Looking for a keyword to activate.
# The keyword is "Hey Computer" and are created using Azures Wakeword service. You can choose other wakewords.
#
#                   Your job:
# Change the path to the wakeword file.
#
#############################################################################################################

import time
import azure.cognitiveservices.speech as speechsdk

def speech_recognize_keyword_locally_from_microphone():
    """runs keyword spotting locally, with direct access to the result audio"""

    # Creates an instance of a keyword recognition model. 
# Update this to point to the location of your keyword recognition model:
    model = speechsdk.KeywordRecognitionModel(r"C:\<Your-PATH>\hey_computer.table")

    # The phrase your keyword recognition model triggers on.
    keyword = "Hey Computer"

    # Create a local keyword recognizer with the default microphone device for input.
    keyword_recognizer = speechsdk.KeywordRecognizer()

    done = False

    def recognized_cb(evt: speechsdk.SpeechRecognitionEventArgs):
        # Only a keyword phrase is recognized. The result cannot be 'NoMatch'
        # and there is no timeout. The recognizer runs until a keyword phrase
        # is detected or recognition is canceled (by stop_recognition_async()
        # or due to the end of an input file or stream).
        result = evt.result
        if result.reason == speechsdk.ResultReason.RecognizedKeyword:
            print("RECOGNIZED KEYWORD: {}".format(result.text))
        nonlocal done
        done = True

    # Connect callbacks to the events fired by the keyword recognizer.
    keyword_recognizer.recognized.connect(recognized_cb)

    # Start keyword recognition.
    result_future = keyword_recognizer.recognize_once_async(model)
    print('Say something starting with "{}" followed by whatever you want...'.format(keyword))
    result = result_future.get()

speech_recognize_keyword_locally_from_microphone()    