#!/usr/bin/python
from time import sleep
import time
import numpy as np
import matplotlib.pyplot as plt
from gpiozero import MCP3208, LED

dev = False
if dev:
    import random

yellowlight = LED(21)
bluelight = LED(26)
redlight = LED(19)

yellowlight.on()
#bluelight.on()
#redlight.on()

adc = MCP3208(channel=1)
secs = 5
voltarray = []

t_end = time.time() + secs
while time.time() < t_end:    
    voltage = 3.3*adc.value

    voltarray.append(voltage)
    print(voltage)

vmean = sum(voltarray)/float(len(voltarray))
vsd = np.std(voltarray)
rsd = vsd/vmean*100

print(' ')
print(vmean)
print(' ')
print(vsd)
print(' ')
print(rsd)
