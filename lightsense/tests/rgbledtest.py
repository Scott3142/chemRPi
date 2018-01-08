import matplotlib.pyplot as plt
from gpiozero import MCP3208, RGBLED
from time import sleep
import time

led = RGBLED(red=19,green=21,blue=26)

#led.red = 1
#sleep(1)
#led.red = 0.5
#sleep(1)

adc = MCP3208(channel=1)
secs = 0.1
voltarray_red = []
voltavgarray_red = []
narray_red = []

voltarray_green = []
voltavgarray_green = []
narray_green = []

voltarray_blue = []
voltavgarray_blue = []
narray_blue = []

led.off()
sleep(1)
for n in range(255):
    led.color = (n/255,0,0)
    t_end = time.time() + secs
    while time.time() < t_end:    
        voltage = 3.3*adc.value
        voltarray_red.append(voltage)

    voltavg_red = sum(voltarray_red)/float(len(voltarray_red))
    narray_red.append(n)
    voltavgarray_red.append(voltavg_red)
    print('n = ' + str(n) + ', vavg = ' + str(voltavg_red) + 'V')

led.off()
sleep(1)
for n in range(255):
    led.color = (0,0,n/255)
    t_end = time.time() + secs
    while time.time() < t_end:    
        voltage = 3.3*adc.value
        voltarray_green.append(voltage)

    voltavg_green = sum(voltarray_green)/float(len(voltarray_green))
    narray_green.append(n)
    voltavgarray_green.append(voltavg_green)
    print('n = ' + str(n) + ', vavg = ' + str(voltavg_green) + 'V')  

led.off()
sleep(1)
for n in range(255):
    led.color = (0,n/255,0)
    t_end = time.time() + secs
    while time.time() < t_end:    
        voltage = 3.3*adc.value
        voltarray_blue.append(voltage)

    voltavg_blue = sum(voltarray_blue)/float(len(voltarray_blue))
    narray_blue.append(n)
    voltavgarray_blue.append(voltavg_blue)
    print('n = ' + str(n) + ', vavg = ' + str(voltavg_blue) + 'V')  
    
plt.plot(narray_red,voltavgarray_red,color='r',linewidth = 1.5)
plt.plot(narray_green,voltavgarray_green,color='g',linewidth = 1.5)
plt.plot(narray_blue,voltavgarray_blue,color='b',linewidth = 1.5)
plt.xlabel('n')
plt.ylabel('V')
plt.xlim(0,255)
plt.show()
