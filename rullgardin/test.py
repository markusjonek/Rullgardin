from gpiozero import Button
import time
from rullgardin import Rullgardin

rullgardin = Rullgardin(4, 22, 27, 26)

print(type(Button(6)))

while True:
    print((rullgardin.knapp.value))

#knapp.wait_for_press()
print('hej')
#for i in range(40):
#    print(knapp.value)
#    time.sleep(0.5)
