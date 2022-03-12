from rullgardin import Rullgardin
from time import sleep
import sys

rullgardin = Rullgardin(4, 22, 17, 26)

def styr():
    riktning = sys.argv[1]
    tid = float(sys.argv[2])
    if riktning == "u":
        rullgardin.upp()
        sleep(tid)
        rullgardin.off()
    if riktning == "n":
        rullgardin.ner()
        sleep(tid)
        rullgardin.off()
styr()
