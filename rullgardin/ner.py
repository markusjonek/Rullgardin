from time import time, sleep
from rullgardin import Rullgardin, Logg, gardiner

def timer_ner(gardin):
    gammal_tid = Logg.read(gardin)
    start = time()
    while True:
        Logg.skriv(str(time()-start), gardin)
        sleep(0.1)
        if time() - start + gammal_tid > gardin.tid:
            Logg.clear(gardin)
            Logg.skriv(str(gardin.tid), gardin)
            break

def main():
    for gardin in gardiner():
        gardin.ner()
        timer_ner(gardin)
        gardin.off()

main()


