# Domoticz with ChatGPT integration
 Control Domoticz with voice commands using ChatGPT
 
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
Start the application when you boot Windows. For your convenience, configure it so it starts before you login.:

Press WINDOWS+R on your keyboard

Enter "taskschd.msc" and press ENTER

Click on "Create Basic Task...", which is located in the section called "Actions"

Now the wizard will help you to create your task - choose the start script AI.bat

Adjust the script's path to where your start.py is.

