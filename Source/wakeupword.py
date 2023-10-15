#############################################################################################################
#                    FUNCTION:
# Looking for a keyword to activate.
# The keyword is "Hey Computer" and are created using Azures Wakeword service. You can choose other wakewords.
# When the keyword are detected, the recogniser stops and the ChatGPT session begins.  
#
#                   Your job:
# Change the path to the wakeword file.
#
#############################################################################################################

import azure.cognitiveservices.speech as speechsdk
import ai

def speech_recognize_keyword_locally_from_microphone():

# Change the path to the wakeword file.
    model = speechsdk.KeywordRecognitionModel(r"C:\<Your-PATH>\hey_computer.table")
    keyword = "Hey Computer"
    keyword_recognizer = speechsdk.KeywordRecognizer()

    # Start keyword recognition.
    result_future = keyword_recognizer.recognize_once_async(model)
    print('Say something starting with "{}" followed by whatever you want...'.format(keyword))
    result = result_future.get()

    if result.reason == speechsdk.ResultReason.RecognizedKeyword:
       # print("RECOGNIZED KEYWORD: {}".format(result.text))
        stop_future = keyword_recognizer.stop_recognition_async()
        stopped = stop_future.get()
        ai.start()
 