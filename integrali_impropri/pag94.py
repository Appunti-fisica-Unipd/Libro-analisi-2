import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


plt.rcParams['text.usetex'] = True #using latex
mpl.rcParams.update({'font.size': 20}) #font size
mpl.rcParams['text.usetex'] = True



fig, ax = plt.subplots()

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -4, 4, -2, 2

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

def function(x):
    return np.array((x - 2) * (x + 3) * (x + 0.1) / 10) 

def functionpos(x):
    return np.where(function(x) > 0, function(x), 0)

def functionneg(x):
    return np.where(function(x) < 0, -function(x), 0)

# Plot function
a=xmin
b=xmax
x = np.arange(a, b, 0.01)
ax.plot(x, function(x), color='k', lw=3)
ax.plot(x, functionpos(x), color='r', ls='--')
ax.plot(x, functionneg(x), color='b', ls='--')


'''# Draw integral area
ix = np.linspace(a, b, num=1000)
iy = function(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, color='r', alpha=0.2)
ax.add_patch(poly)'''

# Use tex in labels
#ax.set_xticks([])
#ax.set_xticklabels([])
#ax.set_yticks([])


# Add text
ax.text(-3.5, 2 , r"$y=f^-(x)$", color='b')
ax.text(3, 1, r"$y=f^+(x)$", color='r')
ax.text(3.5, 2, r"$y=f(x)$", color='k')

equation = r"$f^-(x) = \begin{array}{ll} -f(x) & \text{se } f(x) < 0 \\ 0 & \text{se } f(x) \geq 0 \end{array}$"




plt.show()