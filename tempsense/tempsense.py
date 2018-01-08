#!/usr/bin/python

from gpiozero import MCP3208, LED
from time import sleep
import matplotlib.pyplot as plt

#initialise LED
red_led = LED(17)

#initialise plotting parameters
tint = 0
tplot = []
lplot = []
plt.ion()

delay = 0.05

while True:
  tmp = MCP3208(channel=7)
  temperature = (tmp.value*3.3 - 0.5)*100

  if (temperature >= 25):
    red_led.on()
  else:
    red_led.off()
  
  # Print out results
  print("--------------------------------------------")
  print("Temp: {}C".format(temperature))
  
  tint += delay
  tplot.append(tint)

  lplot.append(temperature)

  plt.plot(tplot,lplot)
  plt.ylim(0,35)
  plt.show()
  plt.pause(delay)
  
