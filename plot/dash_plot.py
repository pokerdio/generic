import scipy
import numpy as np
import matplotlib.pyplot as plt
import ruler

plt.rcdefaults()
plt.style.use("dark_background")

x = np.linspace(0, 10, 500)
dashes = [5, 2,2,2]  # 10 points on, 5 off, 100 on, 5 off

fig, ax = plt.subplots()
line1, = ax.plot(x, np.sin(x), '--', linewidth=2,
                 label='Dashes set retroactively')
line1.set_dashes(dashes)

dashes2 = [5, 2, 2, 2, 2, 2]
line2, = ax.plot(x, -1 * np.sin(x), dashes=dashes2,
                 label='Dashes set proactively')

ax.legend(loc='lower right')
plt.show()
