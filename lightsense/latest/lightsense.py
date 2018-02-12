lsfrom gpiozero import MCP3008, LED import time from time import 
sleep import numpy as np

led = LED(21)
led.on()

sleep(1) #this must be done to make sure LED is lit

adc = MCP3008(channel=1)

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
