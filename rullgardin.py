from gpiozero import LED, Button
from time import time, sleep
import os

logg_path = "/home/pi/Rullgardin/logg/"

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

    def read_log(self):
        fil = open(logg_path + "logg" + self.index + ".txt", encoding="utf8")
        fil_rader = fil.readlines()
        for index, rad in enumerate(fil_rader):
            fil_rader[index] = rad.rstrip("\n")
        if len(fil_rader) < 1:
            print("error i logging för gardin: " + self.index)
            return 0
        return float(fil_rader[-1])

    def log(self, tid):
        with open(logg_path + "logg" + self.index + ".txt", "a") as f:
            f.write(tid)
            f.write("\n")

    def clear_log(self):
        open(logg_path + "logg" + self.index + ".txt", "w").close()

    def ner_logger(self):
        gammal_tid = self.read_log()
        start = time()
        while True:
            try:
                self.log(str(time() - start))
                sleep(0.1)
                if time() - start + gammal_tid > self.tid:
                    self.clear_log()
                    self.log(str(self.tid))
                    break
            except KeyboardInterrupt:
                print("Avbryter")
                break

    def upp_logger(self):
        gammal_tid = self.read_log()
        start = time()
        while self.knapp.value != 1:
            self.log(str(gammal_tid - (time() - start) * 0.87))
            if time() - start > 24:
                self.off()
                self.clear_log()
                self.log("0")
                break
        self.clear_log()
        self.log("0")

def gardiner():
    file = open(logg_path + "gardiner.txt", encoding="utf8")
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


