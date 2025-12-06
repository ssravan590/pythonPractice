import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

a = np.arange(1,20)
b = a**2
plt.plot(a,b,marker='o',linestyle='--',color='blue')
plt.plot(a,a**3,marker='o',linestyle='--',color='yellow')
plt.plot(a,a**4,marker='o',linestyle='--',color='red')
plt.plot(a,a**5,marker='o',linestyle='-.',)
plt.title('square function Line plot')
plt.xlabel('N value')
plt.ylabel('square of N')
plt.show()
