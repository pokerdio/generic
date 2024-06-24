import scipy
import numpy as np
import matplotlib.pyplot as plt


v = np.linspace(0, 6.28, 100, endpoint=False)

#plt.scatter('a', 'b', c='c', s='d', data=data)
plt.scatter(np.sin(v), np.cos(v), c=v, s=np.sin(8 * v)*24+32)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
