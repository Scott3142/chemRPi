from gpiozero import MCP3208, RGBLED
import time
from time import sleep
import numpy as np

led = RGBLED(red=19,green=21,blue=26)
led.color = (0,178/255,1) #specify color

sleep(1) #this must be done to make sure LED is lit

adc = MCP3208(channel=1)

secs = 5 #number of seconds to run 
voltarray = []
voltavgarray = []
narray = []

t_end = time.time() + secs
while time.time() < t_end:
    voltage = 3.3*adc.value
    voltarray.append(voltage)
    print(voltage)

vmean = sum(voltarray)/float(len(voltarray))
vsd = np.std(voltarray)

print(' ')
print(vmean)
print(' ')
print(vsd)
