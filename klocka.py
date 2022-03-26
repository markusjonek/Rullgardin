
from rulla import upp
from time import localtime, sleep
import sys
from gpiozero import LED

led = LED(26)

def klocka():
    if ":" in sys.argv[1]:
        klockslag = sys.argv[1].split(":")
    else:
        klockslag = [sys.argv[1], sys.argv[2]]
    if klockslag[0][0] == "0":
        klockslag[0] = klockslag[0][1]
    if klockslag[1][0] == "0":
        klockslag[1] = klockslag[1][1]

    while True:
        led.on()
        sleep(1)
        led.off()
        if localtime().tm_hour == int(klockslag[0]) and localtime().tm_min == int(klockslag[1]):
            upp()
            break
        sleep(10)


klocka()

