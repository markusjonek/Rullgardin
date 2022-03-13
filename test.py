from gpiozero import Button
import time
from rullgardin import *

rullgardin = gardiner()[1]


while True:
    print((rullgardin.knapp.value))

#knapp.wait_for_press()
print('hej')
#for i in range(40):
#    print(knapp.value)
#    time.sleep(0.5)
