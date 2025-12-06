import matplotlib.pyplot as plt
import numpy as np


plt.figure(num=1,figsize=(10,4),facecolor='yellow')
a = np.arange(1,21)
plt.plot(a,a,'o-r')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
#plt.savefig('drawing.png')