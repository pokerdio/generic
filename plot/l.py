import scipy
import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()
#plt.style.use("dark_background")


species = ('Adelie', 'Chinstrap', 'Gentoo', "foo")
sex_counts = {
    'Male': np.array([73, 34, 61, 25]),
    'Female': np.array([73, 34, 58, 75]),
}
width = 0.6  # the width of the bars: can also be len(x) sequence


fig, ax = plt.subplots()
bottom = np.zeros(len(sex_counts["Male"]))
bottom = -sex_counts["Male"]

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Number of penguins by sex')
ax.legend()

plt.show()
