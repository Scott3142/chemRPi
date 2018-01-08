import matplotlib.pyplot as plt
from scipy import stats

xarray = [1,2,3,4]
yarray = [0.4105564,0.3922838,0.379635,0.368606]

plt.plot(xarray,yarray,marker='o',color='k',markerfacecolor='g')
plt.plot(xarray,yarray,color='r',linewidth=2)
plt.xlabel('Millileters (ml)')
plt.ylabel('Voltage (V)')
plt.xlim(min(xarray),max(xarray))
plt.show()
