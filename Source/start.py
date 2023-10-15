########################################################################
#                    FUNCTION:
# Main program. Runs in a loop, looking for a keyword to activate
#
########################################################################

import wakeupword

def start_assistent():
    while True:  # Create an infinite loop
        wakeupword.speech_recognize_keyword_locally_from_microphone()

start_assistent()
