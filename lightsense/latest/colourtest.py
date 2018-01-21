from gpiozero import MCP3208, RGBLED
from time import sleep

led = RGBLED(red=19,green=21,blue=26)

led.red = 1
sleep(1)
led.off()
sleep(1)
led.green = 1
sleep(1)
led.off()
sleep(1)
led.blue = 1
sleep(1)
led.off()
