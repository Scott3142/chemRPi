#!/usr/bin/python
import matplotlib.pyplot as plt
import os, logging, subprocess, time, argparse
from bottle import route, request, response, redirect, hook, error, default_app, view, static_file, template, HTTPError
import time
import csv

#global parameters and list initialisation
global voltavg,mlplot,vplot,dev,filetime
filetime = time.strftime("%d-%m-%y--%H%M")
vplot = []
mlplot = []

#parameters depending on development environment             
dev = False
if dev:
    import random
else:
    from gpiozero import MCP3208, LED

# define route as hyperlink specified in javascript
@route('/led_toggle')                                                 
def led_toggle():                                                                                              
           
    #deletes plot files from previous run - beware!
    #if file exists
    #os.remove('public/plots/interim.png')
    #os.remove('public/plots/final_plot.png')

    #toggles LED state
    if not dev:
        whitelight = LED(21)
        whitelight.on()
    else:
        print('LED on!')

#gets the simulation runtime from the button click
@route('/get_tlength/<jstlength>')
def get_tlength(jstlength):
    global tlength
    tlength = int(jstlength)

# gets the ml amount from the button click
@route('/get_mlvol/<jsmlvol>')
def get_mlvol(jsmlvol):
    global mlvol
    mlvol = int(jsmlvol)
            
@route('/main_program')
def main_program():
    global mlplot,vplot
    voltavg = get_data(mlvol,tlength,dev) 
    
    #create plotting arrays for final plot
    mlplot.append(mlvol)
    vplot.append(voltavg)

    with open('public/data/' + str(filetime) + '.csv','w') as f:
        writer = csv.writer(f,delimiter='\t')
        writer.writerows(zip(mlplot,vplot))

    return voltavg

def get_data(mlvol,tlength,dev):
    import numpy as np

    # ### runs program to get data from ldr - stores data as array and averages. ### #
    #initialise plotting parameters
    tint = 0
    tplot = []
    voltarray = []
    #plt.ion()

    #initialise time
    time_elapsed = 0
    initial_time = time.time()

    print("Running program. Please wait...")

    #for i in range(1,50):
    while time_elapsed <= tlength:
        if dev:
            voltage = random.uniform(0,1)
        else:
            #gets data from adc - calculating voltage from ldr
            adc = MCP3208(channel=1)
            voltage = 3.3*adc.value
            
        #store and plot
        time_elapsed = time.time() - initial_time
        tint += time_elapsed
        tplot.append(tint)
        voltarray.append(voltage)

    #calculate average voltage across runtime, and print to console
    voltavg = sum(voltarray)/float(len(voltarray))
    print("--------------------------------------------")
    print("Mean Voltage: {}V".format(voltavg))
    #voltsd = np.std(voltarray)
    #print("Standard Deviation: {}V".format(voltsd))
      
    #formats and returns average voltage to get_data function
    return "{:.4f}".format(voltavg)
    
#serve index.html file
@route('/')
def index():
    return static_file('index.html', root='public')

#serve css file
@route('/styles/main.css')
def index():
    return static_file('styles/main.css', root='public')
    
#serve js file
@route('/scripts/main.js')
def index():
    return static_file('scripts/main.js', root='public')
    
#serve js file
@route('/scripts/csvtable.js')
def index():
    return static_file('scripts/csvtable.js', root='public')    
    
#serve data file
@route('/data/' + str(filetime) + '.css')
def index():
    return static_file('/data/' + str(filetime) + '.css', root='public')

#function to set up site on localhost:5000. Handles errors etc.
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # Server settings
    parser.add_argument("-i", "--host", default=os.getenv('IP', '127.0.0.1'), help="IP Address")
    parser.add_argument("-p", "--port", default=os.getenv('PORT', 5000), help="Port")

    # Verbose mode
    parser.add_argument("--verbose", "-v", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    try:
        print('Success.')
    except Exception as e:
        log.error(e)
        exit()

    try:
        app = default_app()
        app.run(host=args.host, port=args.port, server='tornado')
    except:
        log.error("Unable to start server on {}:{}".format(args.host, args.port))
