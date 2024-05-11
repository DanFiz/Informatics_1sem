import numpy as np
import matplotlib.pyplot as plt

species = ('Adelie', 'Chinstrap', 'Gentoo','fsdf')
sex_counts = {
    'Male': np.array([73, 34, 61,42]),
    'Female': np.array([73.1, 34, 58,45]),
}
width = 0.6  # the width of the bars: can also be len(x) sequence


fig, ax = plt.subplots()
bottom = np.zeros(4)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Number of penguins by sex')
ax.legend()

plt.show()