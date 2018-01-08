import matplotlib.pyplot as plt

xarray = [2,4]
yarray = [0.3922838,0.368606]

plt.plot(xarray,yarray,marker='o',color='k',markerfacecolor='g')
plt.plot(xarray,yarray,color='r',linewidth=2)
plt.xlabel('Millileters (ml)')
plt.ylabel('Voltage (V)')
plt.xlim(min(xarray),max(xarray))
plt.show()
