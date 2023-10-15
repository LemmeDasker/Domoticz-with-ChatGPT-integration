# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.

#############################################################################################################
#                    FUNCTION:
# Starts the ChatGPT session.
# Tell ChatGPT it's role and send a question as text.  
#
#                   Your job:
# Provide your own OpenAI API Key.
# Create your own 'system' promp to get ChatGPT to understand what you want it to do.
# Change the 'content' text to your liking.
#############################################################################################################


import openai

def start():

# Provide your own OpenAI API Key.
    openai.api_key = "<Your-API-KEY>"

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
    messages=[
# Create your own 'system' promp to get ChatGPT to understand what you want it to do.
# Change the 'content' text to your liking.
        {"role": "system", "content": "You are a friendly Digital Assistant with a lot of humor."},
        {"role": "user", "content": "How many people live on earth?"}
    ])

    text = chat_completion['choices'][0]['message']['content']
    print(text)

start()



