from gpiozero import MCP3208, RGBLED
import time
import numpy as np

led = RGBLED(red=19,green=21,blue=26)
led.color = (0,178/255,1)

adc = MCP3208(channel=1)

secs = 5
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
rsd = vsd/vmean*100

print(' ')
print(vmean)
print(' ')
print(vsd)
print(' ')
print(rsd)
