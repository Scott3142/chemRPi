from gpiozero import MCP3208, RGBLED
from time import sleep

led = RGBLED(red=19,green=21,blue=26)

adc = MCP3208(channel=1)
led.color = (0,178/255,1)

while True:    
    voltage = 3.3*adc.value
    print(voltage)
