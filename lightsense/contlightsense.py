#!/usr/bin/python
import time, csv
import matplotlib.pyplot as plt

global filetime
filetime = time.strftime("%d-%m-%y--%H%M")

dev = False
if dev:
    import random

def main_program(dev):
    if not dev:
        from gpiozero import LED
        whitelight = LED(21)
        whitelight.on()

    lighton = str(input('Is the LED lit? (y/n) '))
    if lighton != 'y':
        print('Error. Exiting.')
        quit()

    runagain = 'y'
    voltavg = []
    mlvol = []
    readings_okay = 'n'

    tlength = int(input('How long would you like to run the simulations for (s)? '))
    while runagain == 'y':
        mlvol.append(int(input('How many ml do you have? ')))
        while readings_okay == 'n':
            data = getdata(mlvol,tlength,dev)
            readings_okay = str(input('Are you happy with the reading? (y/n) '))
        voltavg.append(data)

        readings_okay = 'n'
        runagain = str(input('Would you like to run another trial? (y/n) '))
        plt.clf()

    if not dev:
        whitelight.off()

    plot_final(mlvol,voltavg)

def getdata(mlvol,tlength,dev):
    if not dev:
        from gpiozero import MCP3208

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

        print(voltage)
        plot_thist(tplot,voltarray,0,tlength)
        plt.pause(0.05)

        with open('data/' + str(filetime) + '.csv','w') as f:
            writer = csv.writer(f,delimiter='\t')
            writer.writerows(zip(tplot,voltarray))

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
    plt.ylim(0,3.5) 
    #plt.xlim(0,tlength)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.show()

def plot_final(mlvol,voltavg):
    plt.plot(mlvol,voltavg,color='b',linewidth = 1.5)
    plt.plot(mlvol,voltavg,'ko',markerfacecolor = 'r')
    plt.xlabel('ml')
    plt.ylabel('V')
    plt.ylim(0,3.5)
    plt.show()

main_program(dev)
wait = input("Press ENTER to end program...")
