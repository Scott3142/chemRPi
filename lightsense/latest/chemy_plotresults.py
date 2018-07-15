from scipy.stats import linregress
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

ymax = 0.3

xarray = [200,600,1000] #change this!
yarray = [0.286617,0.277384,0.270186] #change this!

for i in range(0,len(yarray)):
    yarray[i] = ymax - yarray[i]

pfit = np.polyfit(xarray, yarray, 1)
ffit = np.poly1d(pfit)

xfit = np.linspace(xarray[0],xarray[-1],100)
yfit = ffit(xfit)

#ytest = ?? #change this!

lin = linregress(xarray,yarray)
gradient = lin.slope
intercept = lin.intercept
#xtest = (ytest - intercept)/gradient

#print(lin)
#print('xvalue = ' + str(xtest))

plt.plot(xarray,yarray,marker='o',color='k',markerfacecolor='g')
plt.plot(xarray,yarray,color='r',linewidth=2)
plt.plot(xfit,yfit,color='b',linewidth=2)
#plt.plot(xtest,ytest,marker='x',color='k',markerfacecolor='k')
plt.xlabel('Concentration (mg/L)')
plt.ylabel('Max Voltage - Reading (V)')
plt.xlim(min(xarray),max(xarray))
plt.show()

plt.savefig('chemy-calibration-curve.pdf')
