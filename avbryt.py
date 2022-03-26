from rullgardin import gardiner
import os

for gardin in gardiner():
    gardin.off()

os.system("pkill -9 -f klocka.py")
os.system("pkill -9 -f upp_ner.py")

from gpiozero import LED
import time

led = LED(26)

for i in range(3):
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.3)
