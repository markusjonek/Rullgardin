from rullgardin import *
#from gpiozero import Button

while True:
    knapp1 = str(gardiner()[0].knapp.value)
    knapp2 = str(gardiner()[1].knapp.value)
    print("1: " + knapp1 + " | 2: " + knapp2)

#while True:
#    print(Button(26).value)
