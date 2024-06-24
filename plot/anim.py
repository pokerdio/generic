import scipy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


plt.rcdefaults()
plt.style.use("dark_background")

n = 500

a = 20
b = 100 - a

v = np.ones(10)
v /= np.sum(v)

T = np.linspace(0, np.pi * 4, n)
X = np.sin(T) * a + np.random.random(n) * b



fig, ax = plt.subplots()
line, = ax.plot(T, X, c="r")


# Change the figure title later

fig_title = plt.suptitle('INITIAL DATA')

gen = 0
def animate(i):
    global X, gen
    if (i == 0):
        fig_title.set_text('INITIAL DATA')
        X = np.sin(T) * a + np.random.random(n) * b
    else:
        fig_title.set_text('CONVOLUTION GENERATION %d ' % i)
        X = np.convolve(X, v)[len(v) // 2:n + len(v) // 2]

    line.set_ydata(X)  # update the data
    plt.gcf().canvas.draw()

    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(X)
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(0, 10), init_func=init,
                              interval=1250, blit=True)


plt.show();

