import scipy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mat

plt.rcdefaults()
plt.style.use("dark_background")


animal_names = ['Lion', 'Gazelle', 'Cheetah']
mph_speed = [50, 60, 75]

fig, ax = plt.subplots()
bar_container = ax.bar(animal_names, mph_speed)
ax.set(ylabel='speed in MPH', title='Running speeds', ylim=(0, 80))
ax.bar_label(bar_container, fmt='%.1f m/h')


plt.show()
