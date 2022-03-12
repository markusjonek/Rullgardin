from gpiozero import LED, Button
import time

class Rullgardin:
    def __init__(self, a1, a2, en, knapp, tid, index):
        self.a1 = LED(a1)
        self.a2 = LED(a2)
        self.en = LED(en)
        self.knapp = Button(knapp)
        self.tid = tid
        self.index = str(index)

    def off(self):
        self.en.off()
        self.a1.off()
        self.a2.off()

    def upp(self):
        self.off()
        self.a2.on()
        self.en.on()

    def ner(self):
        self.off()
        self.a1.on()
        self.en.on()

class Logg:
    def read(gardin):
        file = open('/home/pi/Programs/rullgardin/logg' + gardin.index + '.txt', encoding="utf8")
        file_rader = file.readlines()
        ny_fil = []
        for rad in file_rader:
            ny_fil.append(rad.rstrip("\n"))
        return float(ny_fil[-1])

    def skriv(tid, gardin):
        with open('/home/pi/Programs/rullgardin/logg' + gardin.index + '.txt', 'w') as f:
            f.write(tid)
            f.write('\n')

    def clear(gardin):
        open('/home/pi/Programs/rullgardin/logg' + gardin.index + '.txt', 'w').close()

def gardiner():
    file = open('/home/pi/Programs/rullgardin/gardiner.txt', encoding="utf8")
    file_rader = file.readlines()
    rullgardiner = []
    for rad in file_rader:
        rullgardiner.append(rad.rstrip("\n"))
    rullgardiner.pop(0)

    gardiner = []
    for gardin in rullgardiner:
        pinnar = gardin.split()
        index = 1 + rullgardiner.index(gardin)
        a1 = pinnar[0]
        a2 = pinnar[1]
        en = pinnar[2]
        knapp = pinnar[3]
        tid = float(pinnar[4])
        gardiner.append(Rullgardin(a1, a2, en, knapp, tid, index))
    return gardiner


