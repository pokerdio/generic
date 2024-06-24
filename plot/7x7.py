import scipy
import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()

mystyles = ["Solarize_Light2", "bmh", "classic", "dark_background", "fast",
            "fivethirtyeight", "ggplot", "grayscale", "seaborn"]


mylinestyles = ["b-", "g-", "r-"]



if "style_id" not in globals():
    style_id = 0
else:
    #style_id = (style_id + 1) % len(plt.style.available)
    style_id = (style_id + 1) % len(mystyles)

#style_name = plt.style.available[style_id]
style_name = mystyles[style_id]
plt.style.use(style_name)

#plt.style.use("seaborn-dark")



v = [np.linspace(0, np.pi * 2, 200)]
v.append(np.sin(v[0]))
v.append(np.cos(v[0]))
v.append((v[0] - np.pi) ** 2)
v.append((v[0] - np.pi) ** 3)
v.append(v[1] ** 2)
v.append(v[1] * v[2])

fig = plt.figure(figsize=(9,9))
fig.suptitle("style is " + style_name)

k = 0
for i in range(7):
    for j in range(7):
        k += 1
        ax = plt.subplot(7, 7, k)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        plt.plot(v[i], v[j], mylinestyles[k % len(mylinestyles)])

#plt.subplots_adjust(wspace=0.3, hspace=0.6)

plt.show()
