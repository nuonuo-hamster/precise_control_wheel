# 錄音的R鍵，手動移動的QWEASD鍵
from pynput import keyboard
import voiceRecognize
import time

import wheelsHandle
from src import wheel_ctl_base
from src import keyboard_detect

old_key = None

def Wheels_keyboard_trigger(key):
    
    global old_key

    if (key == None and key != old_key):
        msg = wheel_ctl_base.stop()
        wheelsHandle.messageSend(msg)
        time.sleep(0.1)

    if (key == 'w' and key != old_key):
        msg = wheel_ctl_base.forward()
        wheelsHandle.messageSend(msg)
        time.sleep(0.1)

    if (key == 's' and key != old_key):
        msg = wheel_ctl_base.backward()
        wheelsHandle.messageSend(msg)
        time.sleep(0.1)
    
    if (key == 'q' and key != old_key):
        msg = wheel_ctl_base.turnLeft()
        wheelsHandle.messageSend(msg)
        time.sleep(0.1)
    
    if (key == 'e' and key != old_key):
        msg = wheel_ctl_base.turnRight()
        wheelsHandle.messageSend(msg)
        time.sleep(0.1)

    if (key == 'a' and key != old_key):
        msg = wheel_ctl_base.shiftLeft()
        wheelsHandle.messageSend(msg)
        time.sleep(0.1)

    if (key == 'd' and key != old_key):
        msg = wheel_ctl_base.shiftRight()
        wheelsHandle.messageSend(msg)
        time.sleep(0.1)
        
    old_key = key

def Wheels_keyboard_task():

    KBConfig = keyboard_detect.keyboard_config()
    KBConfig.CreateKBDetectTask()

    while(True):
        key = KBConfig.currntKey[0]
        Wheels_keyboard_trigger(key)
        if (key == 'esc'): break

def on_press(key):
    try:
        if key.char == 'r':
            voiceRecognize.startRecording()

    except Exception as e:
        print(f"err while recording: {e}")

def on_release(key):
    try:
        if key.char == 'r':
            voiceRecognize.audioProcess()

    except Exception as e:
        print(f"err while recognization: {e}")

def audioListener():

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':

    audioListener() #press R to record -TW