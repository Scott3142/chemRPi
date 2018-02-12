from gpiozero import MCP3008,LED
from time import sleep

led = LED(21)

adc = MCP3008(channel=1)
led.on()

while True:    
    voltage = 3.3*adc.value
    print(voltage)
    sleep(0.5)
