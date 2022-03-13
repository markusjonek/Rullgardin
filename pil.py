
from rullgardin import *
from sshkeyboard import listen_keyboard
import time

gardin = gardiner()[0]

def press(key):
    if key == "up":
        gardin.upp()
    elif key == "down":
        gardin.ner()

def release(key):
    gardin.off()

listen_keyboard(on_press=press, on_release=release)
