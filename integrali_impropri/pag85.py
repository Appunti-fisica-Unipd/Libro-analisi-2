import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

plt.rcParams['text.usetex'] = True #using latex
matplotlib.rcParams.update({'font.size': 20}) #font size

fig, ax = plt.subplots()#figsize=(10, 10))

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -.1, 5.5, -.1, 5.5

# Set identical scales for both axes
ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=1)

# Set bottom and left spines as x and y axes of coordinate system
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Create 'x' and 'y' labels placed at the end of the axes
ax.set_xlabel('$x$', labelpad=-24, x=1.03)
ax.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)

# Draw arrows
arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

x = []
y = []
for i in range(1,6):
    x = x + [i, i + 1/(2*2**i), i + 1/(2**i)]
    y = y + [0, i, 0]

print(x, '\n', y)

# Plot function
plt.plot(x, y, color='r')

# Draw integral area
ix = x
iy = y
verts = [(0, 0), *zip(ix, iy), (5, 0)]
poly = Polygon(verts, color='r', alpha=0.2)
ax.add_patch(poly)

# Draw lines to axis
for i in range(1,6):
    ax.plot([i + 1/(2*2**i), 0], [i, i], ls="--", lw=1, color='k')

# Use tex in labels
ax.set_xticks([x[0], x[2], x[3], x[5], x[6], x[8], x[9], x[11], x[12], x[14]])
ax.set_xticklabels([r"$1$", r"$\frac{3}{2}$", r"$2$", "", r"$3$", "", r"$4$", "", r"$n$", ""], color="k")
ax.set_yticks([y[1], y[4], y[7], y[10], y[13]])

# Add text
ax.text(2.1, -.3 , r"base $\frac{1}{4}$", color='b', size=10)
ax.text(3.1, -.3 , r"base $\frac{1}{2^3}$", color='b', size=10)
ax.text(5.1, .5 , r"base $\frac{1}{2^n}$", color='b', size=10)

plt.show()