from rullgardin import Rullgardin, Logg, gardiner 
from upp import upp
from time import localtime, sleep
import sys

def klocka():
    klockslag = [int(sys.argv[1]), int(sys.argv[2])]
    while True:
        if localtime().tm_hour == klockslag[0] and localtime().tm_min == klockslag[1]:
            upp()
            break
        sleep(10)

klocka()

