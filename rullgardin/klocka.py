from rullgardin import Rullgardin, Logg, gardiner 
from time import localtime, sleep
import sys

def upp():
    for gardin in gardiner():
        gardin.upp()
        gardin.knapp.wait_for_press()
        gardin.off()
        Logg.skriv('0', gardin)

def main():
    klockslag = [int(sys.argv[1]), int(sys.argv[2])]
    while True:
        if localtime().tm_hour == klockslag[0] and localtime().tm_min == klockslag[1]:
            upp()
            break
        sleep(50)

main()

