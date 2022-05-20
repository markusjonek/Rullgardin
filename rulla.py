from rullgardin import *
from time import sleep
from threading import Thread
import sys
import os
from paramiko import SSHClient, AutoAddPolicy

CLIENT = SSHClient()
CLIENT.load_host_keys("/home/pi/.ssh/known_hosts")
CLIENT.load_system_host_keys()
CLIENT.set_missing_host_key_policy(AutoAddPolicy())
CLIENT.connect("mjonek.duckdns.org", username="markus")

GARDINER = gardiner()

def upp_thread(gardin):
    gardin.upp()
    gardin.knapp.wait_for_press()
    gardin.off()
    sleep(0.1)
    gardin.ner()
    sleep(0.2)
    gardin.off()

def ner_thread(gardin):
    gardin.ner()
    sleep(gardin.tid)
    gardin.off()

def upp(gardiner):
    for gardin in gardiner:
        Thread(target=upp_thread, args=(gardin,)).start()

def ner(gardiner):
    for gardin in gardiner:
        Thread(target=ner_thread, args=(gardin,)).start()

def reset_log():
    stdin, stdout, stderr = CLIENT.exec_command("echo 0 > rullgardin_log.txt")
    stdin.close()

def main():
    for gardin in GARDINER:
        gardin.off()
    reset_log()
    funcs = {"ner": ner, "upp": upp}
    while True:
        stdin, stdout, stderr = CLIENT.exec_command("cat rullgardin_log.txt")
        stdin.close()
        cmd = stdout.readlines()[0].rstrip("\n")
        if cmd in funcs:
            funcs[cmd](GARDINER)
            reset_log()
        elif len(cmd) > 3 and cmd[0:3] in funcs:
            func = funcs[cmd[0:3]]
            gardin = [GARDINER[int(cmd[-1]) - 1]]
            func(gardin)
            reset_log()
        elif cmd == "stop":
            for gardin in GARDINER:
                gardin.off()
            reset_log()
        sleep(0.1)


if __name__ == '__main__':
    main()
