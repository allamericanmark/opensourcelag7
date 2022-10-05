import subprocess
import time
import keyboard

WIFI_NAME=''
with open('wifiname.txt') as o:
    WIFI_NAME = o.read()
print('Using wifi network:',WIFI_NAME)

LAG_BUTTON=''
with open('lagbutton.txt') as o:
    LAG_BUTTON = o.read()
print('Using lag button:',LAG_BUTTON)

def lag7():
    def disconnect():
        process = subprocess.Popen(
            'netsh wlan disconnect',
            shell = True,
            stdout = subprocess.PIPE, 
            stderr = subprocess.PIPE)
        process.communicate()
    def connect():
        process = subprocess.Popen(
            'netsh wlan connect {0}'.format(WIFI_NAME),
            shell = True,
            stdout = subprocess.PIPE, 
            stderr = subprocess.PIPE)
        process.communicate()
    disconnect()
    print("Waiting to reconnect...")
    time.sleep(7)
    connect()
    print("Reconnected.")

while True:
    if keyboard.is_pressed("F10"):
        print("F10 pressed, starting lag...")
        lag7()
    time.sleep(0.5)