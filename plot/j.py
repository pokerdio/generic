import scipy
import numpy as np
import matplotlib.pyplot as plt
import ruler

# plt.rcdefaults()
# x = np.linspace(0, 6, 100)
# y = np.sin(x)

# cmap = cmaps[np.random.randint(len(cmaps))]
# plt.scatter(x, y, c=y, cmap=cmap)
# plt.colorbar(label=cmap)
# plt.show(block=True)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = 2 * np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center',
#         color='green', ecolor='black')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show(block = True);


# plt.style.use("dark_background")

# x = np.linspace(0, 2, 500)
# y = 0.5 + 3 * np.sin(4 * np.pi * x) * np.exp(-2 *  x)

# y2 = 0.2 + np.sin(6 * np.pi * x) * np.exp(1.2 *  x)

# y3 = -1.5 + 1.6 * np.sin(12 * np.pi * x)

# fig, ax = plt.subplots()
# ax.yaxis.grid(color='gray', linestyle='dashed')
# ax.xaxis.grid(color='gray', linestyle='dashed')

# ax.set_axisbelow(False)



# ax.grid(True, zorder=25)
# # ax.fill(x, y, zorder=1.2)
# # ax.fill(x, y2, zorder=1.3)
# # ax.fill(x, y3, zorder=2.4)
# ax.fill(x, y, "g", x, y2, "y", zorder=2.4, alpha=0.8)
# plt.show()


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
