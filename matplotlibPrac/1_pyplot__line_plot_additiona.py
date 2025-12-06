import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

a = np.arange(1,11)
b = a**2
plt.plot(a,b,marker='o',linestyle='--',color='blue')
plt.title('square function Line plot')
plt.xlabel('N value')
plt.ylabel('square of N')
plt.show()
