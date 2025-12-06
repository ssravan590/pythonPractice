import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

a = np.arange(1,20)
b = a**2
plt.plot(a,b,'o-r') # cirle o-line and red color mlc or cml i.e o-r or ro-
plt.plot(a,a**3,'y-o',lw=10,ms=15,mfc='red',alpha=0.1)

plt.title('square function Line plot')
plt.xlabel('N value')
plt.ylabel('square of N')
plt.show()
