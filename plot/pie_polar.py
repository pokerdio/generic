import matplotlib.pyplot as plt

plt.rcdefaults()
#plt.style.use("dark_background")
# Compute pie slices
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 16 * np.random.rand(N) + 0.1

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)

# Use custom colors and opacity
for i, r, bar in zip(range(len(radii)), radii, bars):
    bar.set_facecolor(plt.cm.Oranges(width[i] / max(width)))
    bar.set_alpha(0.9)

plt.show()
