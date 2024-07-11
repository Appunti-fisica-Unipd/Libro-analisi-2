import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

plt.rcParams['text.usetex'] = True #using latex
matplotlib.rcParams.update({'font.size': 20}) #font size

fig, ax = plt.subplots()#figsize=(10, 10))

r = 300

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -.1, 1.1, -r, r

# Set identical scales for both axes
ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=.5/r)

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

def function(x):
    return np.array(np.sin(1/x)/x**2)

def limiters(x):
    return np.array(1/x**2)

# Plot function
c = 0.05
a = 0.06
b = 1
x = np.arange(c, b + 0.1, 0.001)
plt.plot(x, function(x), color='r')
plt.plot(x, limiters(x), color='b', ls='--')
plt.plot(x, -limiters(x), color='b', ls='--')

# Draw lines connecting points to axes
#ax.plot([a, a], [0, function(a)], c='k', ls='--', lw=1.5, alpha=0.5)
#ax.plot([b, b], [0, function(b)], c='k', ls='--', lw=1.5, alpha=0.5)

# Add text
ax.text(.8, 30 , r"$y=\frac{\sin\frac{1}{x}}{x^2}$", color='r')
ax.text(.1, 250, r"$y=\frac{1}{x^2}$", color='b')
ax.text(.1, -250, r"$y=-\frac{1}{x^2}$", color='b')


# Draw integral area
ix = np.linspace(a, b, num=1000)
iy = function(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, color='r', alpha=0.2)
ax.add_patch(poly)

# Use tex in labels
ax.set_xticks([b])
ax.set_xticklabels(["$1$"], color="k")
ax.set_yticks([])

plt.show()