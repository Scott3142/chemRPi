import matplotlib.pyplot as plt
from sympy import S, symbols
from scipy.stats import linregress
import sympy as sp
import numpy as np

#xarray = [0.5,1,2.5,5,10,15,20]
#yarray = [0.44113,0.439456,0.43331,0.42637,0.414342,0.40452,0.39608]

xarray = [5,10,15,20]
yarray = [0.424089,0.4089336,0.400872,0.39379]

pfit = np.polyfit(xarray, yarray, 1)
ffit = np.poly1d(pfit)

xfit = np.linspace(xarray[0],xarray[-1],100)
yfit = ffit(xfit)

yirn = 0.4032922
lin = linregress(xarray,yarray)
gradient = lin.slope
intercept = lin.intercept
xirn = (yirn - intercept)/gradient

print(lin)
print('xvalue = ' + str(xirn))

plt.plot(xarray,yarray,marker='o',color='k',markerfacecolor='g')
plt.plot(xarray,yarray,color='r',linewidth=2)
plt.plot(xfit,yfit,color='b',linewidth=2)
plt.plot(xirn,yirn,marker='x',color='k',markerfacecolor='k')
plt.xlabel('Miligrams per litre (mg/L)')
plt.ylabel('Voltage (V)')
plt.xlim(min(xarray),max(xarray))
#plt.show()

plt.savefig('calibration-curve.pdf')
