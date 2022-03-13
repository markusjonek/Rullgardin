from rullgardin import Rullgardin, Logg, gardiner
from time import time, sleep
import threading

def stop_check(gardin):
    gardin.knapp.wait_for_press()
    gardin.off()

def time_logger(gardin):
    innan_start = Logg.read(gardin)
    start = time()
    stopp_checker = threading.Thread(target=stop_check, args=(gardin,))
    stopp_checker.start()
    while stopp_checker.is_alive():
        Logg.skriv(str(innan_start - (time() - start)*0.87), gardin)
        sleep(0.1)
        if time()-start > 24:
            gardin.off()
    Logg.clear(gardin)
    Logg.skriv('0', gardin)

def gardin_upp(gardin):
    gardin.upp()
    time_logger(gardin)
    gardin.off()
    sleep(0.3)
    gardin.ner()
    sleep(0.2)
    gardin.off()

def upp():
    for gardin in gardiner():
        threading.Thread(target=gardin_upp, args=(gardin,)).start()

if __name__ == '__main__':
    upp()
