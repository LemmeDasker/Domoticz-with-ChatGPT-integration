# Domoticz with ChatGPT integration
Control Domoticz with voice commands using ChatGPT!

![IMG_1114-min (3)](https://github.com/LemmeDasker/Domoticz-with-ChatGPT-integration/assets/38005465/7ec26f82-0fc8-4b39-9832-5dd76f6a0731)





We all know Alexa and Google Home, but they are pretty dumb devices, even though they do the job well. They can switch the light On-/Off, but can only take one command at a time. And you have to be fairly precise in your command.

Adding the extra AI layer we have seen with ChatGPT where the digital assistant can understand the spoken context and handle multiple requests simultaneously is groundbreaking. Unfortunately, we might be looking a year or two ahead of this integration.

But look no more...now you can make it yourself.

This is the code that will make you start the integration. You can add more devices and twist it to suit your specific needs.

In my current setup (and not with this basic code), I can speak to Domoticz and for example give it commands like turning different lamps on/off and change their light intensity, all in the same sentence. It can give me the status of all or individual doors if they are open/closed, and it can also function as a traditional digital assistant answering questions.

It still comes with minor errors occasionally, but it seems to come down to two things:

A good speaker/microphone. If you can, choose a Conference model with 4 directional microphones and good noise reduction. I use a Jabra Speak2 40 UC. 

ChatGPT's ability to recognise the spoken context and convert it to the correct commands. This will get better as OpenAI matures the LLM model. Right now I use ChatGPT4.

### Install the needed packages 
#### Microsoft Visual C++ Redistributable
Install the Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017, 2019, and 2022.
https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170&preserve-view=true#visual-studio-2015-2017-2019-and-2022

#### Python
Install a version of Python from 3.7 or later. Remember to 'Add to PATH' and optionally 'Disable PATH lenght' during installation.
```
https://www.python.org/downloads/
```

#### Python HTTP library
Install a version of the HTTP Python library:
```
python -m pip install requests
```

#### Azure Speech SDK for Python
Install the Speech SDK for Python. To install the Speech SDK for Python, run this command in a console window:
```
pip install azure-cognitiveservices-speech
pip install --upgrade azure-cognitiveservices-speech
```

#### Custom Keyword
Create your own custom keyword that will act as your wakeword. You can also just use the one provided called 'Hey, Computer'.
```
https://speech.microsoft.com/portal/5a53969f7b5b4524a7dcadbcc7332234/customkeyword
```

#### Install the OpenAI Python library:
```
pip install --upgrade openai
```

#### Start script
You start the application by opening a command promt, going to your folder with your project at run: python start.py

When you are finished with testing and want to 'go live', I recommend you start the application when you boot Windows. For your convenience, configure it so it starts before you login.:

Press WINDOWS+R on your keyboard

Enter "taskschd.msc" and press ENTER

Click on "Create Basic Task...", which is located in the section called "Actions"

Now the wizard will help you to create your task - choose the start script AI.bat

Adjust the script's path to where your start.py is.

