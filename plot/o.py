import scipy
import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()
plt.style.use("dark_background")

n = 100

a = 70
b = 100 - a

v = np.ones(10)
v /= np.sum(v)

T = np.linspace(0, np.pi * 4, n)
X = np.sin(T) * a + np.random.random(n) * b
for i in range(10):
    Y = np.convolve(X, v)[len(v) // 2:n + len(v) // 2]

plt.plot(T, X, c="r");
plt.plot(T, Y, c="c");
plt.show();
