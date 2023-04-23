import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np
a = np.array([[4,8,5,7,6],[2,3,4,2,6],[4,7,4,7,8],[2,6,4,8,6],[2,4,3,3,2]])

df = DataFrame(a,columns=['a','b','c','d','e'],index=[2,4,6,8,10])
print(df)

df.plot(kind='bar')

plt.title('Bar Graph using DataFrame')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.minorticks_on()
plt.grid(which='major',linewidth=0.5,linestyle="-",color='red')
plt.grid(which='minor',linestyle=':',linewidth=0.5,color='black')

plt.show()
