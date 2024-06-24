import scipy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


plt.rcdefaults()
plt.style.use("dark_background")

a = 80
b = 100 - a
n = 250

T = np.linspace(0, np.pi * 2, n)
X = np.sin(T) * a + np.random.random(n) * b
Y = np.cos(T) * a + np.random.random(n) * b


plt.scatter(X, Y, c = "y", s=150, marker="*");
plt.show();

plt.plot(T, X, c="r");
plt.plot(T, Y, c="c");
plt.show();
