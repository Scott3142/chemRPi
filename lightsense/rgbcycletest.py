import matplotlib.pyplot as plt
from gpiozero import MCP3208, RGBLED
from time import sleep
import numpy as np
import time

adc = MCP3208(channel=1)
led = RGBLED(red=19,green=21,blue=26)

secs = 0.05
voltarray = []
voltavgarray = []
countarray = []

redval,blueval,greenval = 255,0,0
nmax = 3*255-1

for counter in range(nmax):
    led.color = (redval/255,greenval/255,blueval/255)
    
    t_end = time.time() + secs
    while time.time() < t_end:    
        voltage = 3.3*adc.value
        voltarray.append(voltage)

    voltavg = sum(voltarray)/float(len(voltarray))
    countarray.append(counter)
    voltavgarray.append(voltavg)
    print('n = ' + str(counter) + ', vavg = ' + str(voltavg) + 'V')
    
    if counter < 255:
        redval -= 1
        greenval += 1
        blueval = 1
    elif counter < 509:
        redval = 1
        greenval -= 1
        blueval += 1
    elif counter < 763:
        redval += 1
        greenval = 1
        blueval -= 1

led.off()

plt.plot(countarray,voltavgarray,color='k',linewidth = 1.5)
plt.xlabel('n')
plt.ylabel('V')
plt.xlim(0,nmax)
plt.show()
    
