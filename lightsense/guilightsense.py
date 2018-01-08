#!/usr/bin/python
import matplotlib.pyplot as plt
from guizero import App, yesno, error, Text, TextBox, Slider, PushButton

dev = True
if dev:
    import random
else:
    from gpiozero import MCP3208
    from gpiozero import LED

def main_program(dev):
    
    if not dev:
        whitelight = LED(21)
        whitelight.on()
    
    app = App(title="Chemistry Outreach Project v1.1")
    lighton = yesno("Initialisation check.","Is the LED lit?")
    if not lighton:
        error("Initialisation error.","Please check the connections and run the program again.")
        quit()
    app.destroy()

    tlength = int(input('How long would you like to run the simulations for (s)? '))
    run_program(tlength)

    if not dev:
        whitelight.off()

def run_program(tlength):

    runagain = True        
    readings_okay = False
    voltavg = []                                                                                          
    mlvol = []                                                                                            
                                                                        
    while runagain:                                                                                
        mlvol.append(int(input('How many ml do you have? ')))
        while not readings_okay:                                                                       
            data = getdata(mlvol,tlength,dev)
            readings_okay = yesno("Reading check.","Are you happy with the reading?")
        voltavg.append(data)                                                                              
        readings_okay = False                       
        runagain = yesno("Run again check.","Would you like to run another trial?") 
        plt.clf() 

    plot_final(mlvol,voltavg)  

def getdata(mlvol,tlength,dev):
    import time
    import numpy as np

    #initialise plotting parameters
    tint = 0
    tplot = []
    voltarray = []
    plt.ion()

    time_elapsed = 0
    initial_time = time.time()

    print("Running program. Please wait...")

    #for i in range(1,50):
    while time_elapsed <= tlength:
        if dev:
            voltage = random.uniform(0,1)
        else:
            adc = MCP3208(channel=1)
            voltage = 3.3*adc.value
        
        time_elapsed = time.time() - initial_time
        tint += time_elapsed
        tplot.append(tint)
        voltarray.append(voltage)

    voltavg = sum(voltarray)/float(len(voltarray))
    print("--------------------------------------------")
    print("Mean Voltage: {}V".format(voltavg))
    #voltsd = np.std(voltarray)
    #print("Standard Deviation: {}V".format(voltsd))

    plot_thist(tplot,voltarray,voltavg,tlength)

    return voltavg

def plot_thist(tplot,voltarray,voltavg,tlength):
    plt.plot(tplot,voltarray,'b',linewidth = 1.5)
    plt.axhline(y=voltavg,xmin=tplot[0],xmax=tplot[-1],color='r',linewidth=1.5)
    plt.ylim(0,3.3) 
    plt.xlim(0,tlength)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.show()

def plot_final(mlvol,voltavg):
    plt.plot(mlvol,voltavg,color='b',linewidth = 1.5)
    plt.plot(mlvol,voltavg,'ko',markerfacecolor = 'r')
    plt.xlabel('ml')
    plt.ylabel('V')
    plt.ylim(0,3.3)
    plt.show()

main_program(dev)
wait = input("Press ENTER to end program...")
