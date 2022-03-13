from rullgardin import gardiner
from time import sleep
from threading import Thread
import sys

def upp_thread(gardin):
    gardin.upp()
    gardin.upp_logger()
    gardin.off()
    sleep(0.1)
    gardin.ner()
    sleep(0.2)
    gardin.off()

def ner_thread(gardin):
    gardin.ner()
    gardin.ner_logger()
    gardin.off()

def upp():
    for gardin in gardiner():
        Thread(target=upp_thread, args=(gardin,)).start()

def ner():
    for gardin in gardiner():
        Thread(target=ner_thread, args=(gardin,)).start()

def main():
    riktning = sys.argv[1]
    if len(sys.argv) == 1:
        if riktning == "ner":
            ner()
        elif riktning == "upp":
            upp()
    elif len(sys.argv) > 1:
        gardin = gardiner()[int(sys.argv[2])]
        if riktning == "ner":
            ner_thread(gardin)
        elif riktning == "upp":
            upp_thread(gardin)

if __name__ == '__main__':
    main()
