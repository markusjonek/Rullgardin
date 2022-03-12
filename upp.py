from rullgardin import Rullgardin, Logg, gardiner
from time import time, sleep
import threading

def time_logger(gardin):
    innan_start = Logg.read(gardin)
    start = time()
    while True:
        Logg.skriv(str(innan_start - (time() - start)*0.87), gardin)
        sleep(0.05)
        if gardin.knapp.value == 1:
            Logg.clear(gardin)
            Logg.skriv('0', gardin)
            break

def gardin_upp(gardin):
    gardin.upp()
    time_logger(gardin)
    gardin.off()

def main():
    for gardin in gardiner():
        threading.Thread(target=gardin_upp, args=(gardin,)).start()

main()
