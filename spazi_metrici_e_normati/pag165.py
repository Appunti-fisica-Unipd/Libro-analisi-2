import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 

plt.rcParams['text.usetex'] = True #using latex
mpl.rcParams.update({'font.size': 20}) #font size

fig, ax1 = plt.subplots()

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -.1, 2, -.1, 2

# Set identical scales for both axes
ax1.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=1)

# Set bottom and left spines as x and y axes of coordinate system
ax1.spines['bottom'].set_position('zero')
ax1.spines['left'].set_position('zero')

# Remove top and right spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Create 'x' and 'y' labels placed at the end of the axes
ax1.set_xlabel('$x$', labelpad=-24, x=1.03)
ax1.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)

# Draw arrows
arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax1.plot((1), (0), marker='>', transform=ax1.get_yaxis_transform(), **arrow_fmt)
ax1.plot((0), (1), marker='^', transform=ax1.get_xaxis_transform(), **arrow_fmt)

n = .6

# Plot lines
ax1.plot([0, 1/(2 * n)], [0, (2 * n) / np.sqrt(2 * n) * 1 / (2 * n)], color="b")
ax1.plot([1/(2 * n), 1 / n], [(2 * n) / np.sqrt(2 * n) * 1 / (2 * n), 0], color="b")
ax1.plot([1 / n, 1], [0, 0], color="b")
ax1.plot([1/8, 1/8], [2, 2], color="b", ls="--")

x = np.linspace(.001, 1)

def rfun(x):
    return np.array(1 / np.sqrt(x))

ax1.plot(x, rfun(x), color="r")

# Use tex in labels
ax1.set_xticks([1 / (2 * n), 1 / n, 1])
ax1.set_xticklabels([r"$\frac{1}{2n}$", r"$\frac{1}{n}$", r"$1$"])
ax1.set_yticks([])
ax1.set_yticklabels([])



#Add text
ax1.text(1/4, 1, r"$y=g_n(x)$", color="r")






plt.tight_layout()
plt.show()