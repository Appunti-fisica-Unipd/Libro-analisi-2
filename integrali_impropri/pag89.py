import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

plt.rcParams['text.usetex'] = True #using latex
matplotlib.rcParams.update({'font.size': 20}) #font size

fig, ax = plt.subplots()

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -5, 5, -.1, 4

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

def function1(x):
    return np.array(np.e**x)

def function2(x):
    return np.array(1 / (x * np.sqrt(x - 1)))

# Plot function
a=xmin
b=1
c=.1
d=xmax
x1 = np.arange(a, b, 0.01)
x2 = np.arange(c, d, 0.01)
ax.plot(x1, function1(x1), color='r')
ax.plot(x2, function2(x2), color='r')


# Draw axis x = 1
ax.vlines(x=1, ymin=ymin, ymax=ymax, color='b')


'''# Draw integral area
ix = np.linspace(a, b, num=1000)
iy = function(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, color='r', alpha=0.2)
ax.add_patch(poly)'''

# Use tex in labels
ax.set_xticks([-4, 1, 4])
ax.set_xticklabels([r"$-\infty$", r"$1$", r"$+\infty$"], color="b")
ax.set_yticks([])


# Add text
ax.text(-2.5, .5 , r"$y=e^x$", color='r')
ax.text(2, 1, r"$y=\frac{1}{x \sqrt{x-1}}$", color='r')


plt.show()