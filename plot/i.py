import scipy
import numpy as np
import matplotlib.pyplot as plt


# t = np.arange(0.2, 2.0, 0.1)

# plt.plot(t, t, "bo-", t, t ** 2, "g^", t, t ** 3, "r--")
# plt.show()


data = {'a': np.arange(50),
        'c': np.random.randint(50, 100, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

#plt.scatter('a', 'b', c='c', s='d', data=data)
plt.scatter(data["a"], data["b"], c=data["c"], s=data["d"], cmap="Oranges", vmin=0, vmax=100)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.colorbar(label="colorbar label", ticks = range(3, 100, 18))
plt.show()
