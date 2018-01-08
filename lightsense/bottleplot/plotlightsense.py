#!/usr/bin/python
import matplotlib.pyplot as plt
import os, logging, subprocess, time, argparse
from bottle import route, request, response, redirect, hook, error, default_app, view, static_file, template, HTTPError
import time

#global parameters and list initialisation
global voltavg,mlplot,vplot,dev
vplot = []
mlplot = []

#parameters depending on development environment             
dev = True
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
        whitelight.toggle()
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
    global vplot
    voltavg = get_data(mlvol,tlength,dev) 
    
    #create plotting arrays for final plot
    mlplot.append(mlvol)
    vplot.append(voltavg)
    filename = 'public/plots/final_plot.png'
    plot_final(mlplot,vplot,filename)

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

    #plots time history and sets filename
    filename = 'public/plots/interim.png'
    plot_thist(tplot,voltarray,voltavg,tlength,filename)
      
    #formats and returns average voltage to get_data function
    return "{:.4f}".format(voltavg)

#generates time history image, and overwrites interim/.png in public/ directory. 
@route('/<filename:re:.*\.png>')
def plot_thist(tplot,voltarray,voltavg,tlength,filename):
    plt.plot(tplot,voltarray,'b',linewidth = 1.5)
    plt.axhline(y=voltavg,xmin=tplot[0],xmax=tplot[-1],color='r',linewidth=1.5)
    plt.ylim(0,3.3) 
    plt.xlim(0,tlength)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    #plt.show()
    plt.savefig(filename)
    plt.clf()
    return static_file(filename, root='./plots', mimetype='image/png')

#generates final plot, with average voltage against mls
@route('/<filename:re:.*\.png>')
def plot_final(mlplot,vplot,filename):
    plt.plot(mlplot,vplot,color='b',linewidth = 1.5)
    plt.plot(mlplot,vplot,'ko',markerfacecolor = 'r')
    plt.xlabel('ml')
    plt.ylabel('V')
    plt.ylim(0,3.3)
    #plt.show()
    plt.savefig(filename)
    plt.clf()
    return static_file(filename, root='./plots', mimetype='image/png')

# ### return static files ### #
#serve png images
@route('/interim.png')
def index():
    return static_file('interim.png', root='public/plots')

@route('/final_plot.png')
def index():
    return static_file('final_plot.png', root='public/plots')

#serve index.html file
@route('/')
def index():
    return static_file('index.html', root='public')

#serve css file
@route('/style.css')
def index():
    return static_file('style.css', root='public')

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
