import scipy
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(6,6))
ax = plt.subplot(aspect=0.5)
ax.plot(list(x * x for x in np.arange(-5, 6, 0.2)))
plt.xlabel("HELLO WORLD")
plt.savefig("c.png")
plt.show()
