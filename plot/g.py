import matplotlib.pyplot as plt
from numpy.random import rand

plt.rcdefaults()
plt.style.use("dark_background")

fig, ax = plt.subplots()
for color in ['red', 'green', 'blue']:
    n = 150
    x, y = rand(2, n)
    scale = 100.0 * rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.7, edgecolors='white')

ax.legend()
ax.grid(True)

plt.show()
