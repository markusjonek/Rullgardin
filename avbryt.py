from rullgardin import Rullgardin
import os

Rullgardin(4, 22, 17, 26).off()

os.system("pkill -9 -f klocka.py")
os.system("pkill -9 -f ner.py")
os.system("pkill -9 -f upp.py")
