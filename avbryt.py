from rullgardin import gardiner
import os

for gardin in gardiner():
    gardin.off()

os.system("pkill -9 -f klocka.py")
os.system("pkill -9 -f upp_ner.py")
