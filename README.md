# Keylogger
A functionality that will capture the keyboard activity of a user, i.e. Keylogging

**1. System Keylogger:**
_Modules used:
Python - "keyboard", "subprocess", "sys", "os", "requests"
Node - "express", "cors", "body-parser"_

Python file which automates the installation of the "keyboard" module even when it is not installed on a computer. Once the installation is done, it will automatically start logging the keystrokes done on your computer provided the python terminal is running in the background. 
Furthermore, it will send all the keylogs to a local server (server.js). 
Addtionally, it will also save the keylogs to a file "keylogs.txt". 

**2. Website Keylogger: **
_Modules used: "flask", "request", "json", "CORS" _

A webpage when opened will continue logging all the keystrokes provided you are ON the webpage. 
It prints the keys pressed to the console and sennds it to a local server (server.py). 
Addtionally, it will log the keystrokes in a file named "keys.txt" 

**3. Terminal Keylogger: **
_Modules used:
Python - "flask", "request"
Node - "keypress", "axios"_

Terminal based keylogger which logs all the keystrokes by a user. This functionality only works if the user has cursor on the terminal window. 
Additionally, it will send all the keystrokes to a local server (server.py)

These keyloggers can be interfaced as per requirements to build a full fledged keylogger with all components and functionalities intact. 
