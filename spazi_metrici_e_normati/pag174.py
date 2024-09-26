from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.patches as patches


plt.rcParams['text.usetex'] = True #using latex
params = {'font.size': 20, 'text.latex.preamble' : r"\usepackage{amsmath}"}
#font size
pyplot.rcParams.update(params)


fig, ax1 = plt.subplots()

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -5, 5, -2, 2

# Set identical scales for both axes
ax1.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=1)

# Set bottom and left spines as x and y axes of coordinate system
ax1.spines['bottom'].set_position('zero')
ax1.spines['left'].set_position('zero')

# Remove top and right spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)


# Create 'x' and 'y' labels placed at the end of the axes
#ax1.set_xlabel('$x$', labelpad=-24, x=1.03)
#ax1.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)

# Draw arrows
#arrow_fmt = dict(markersize=4, color='black', clip_on=False)
#ax1.plot((1), (0), marker='>', transform=ax1.get_yaxis_transform(), **arrow_fmt)
#ax1.plot((0), (1), marker='^', transform=ax1.get_xaxis_transform(), **arrow_fmt)


# Use tex in labels

ax1.set_xticks([])
ax1.set_xticklabels([])
ax1.set_yticks([])
ax1.set_yticklabels([])


ax1.scatter([-3], [0], color="b", marker='.')
ax1.scatter([3], [0], color="b", marker='.')


e1 = patches.Ellipse([-3, 0], 3, 2, angle=22.5, edgecolor=(0, 0, 0, 1), facecolor=(0, 0, 0, 0))
c1 = patches.Circle([-3, 0], .5, edgecolor=(0, 1, 0, 1), facecolor=(1, 1, 1, 0))
e2 = patches.Ellipse([3, 0], 3, 2, angle=-22.5, edgecolor=(0, 0, 0, 1), facecolor=(0, 0, 0, 0))
c2 = patches.Circle([3, 0], .5, edgecolor=(1, 0, 0, 1), facecolor=(1, 1, 1, 0))

fa1 = patches.FancyArrowPatch((-3.3, 0.2), (3.3, 0), connectionstyle="arc3, rad=-.1", color="orange", arrowstyle="simple, head_width=5, head_length=10")
fa2 = patches.FancyArrowPatch((-2.7, 0), (2.7, 0), connectionstyle="arc3, rad=-.1", color="orange",  arrowstyle="simple, head_width=5, head_length=10")
fa3 = patches.FancyArrowPatch((-3, 0.4), (3, 0.4), connectionstyle="arc3, rad=-.05", color="orange", arrowstyle="simple, head_width=5, head_length=10")
fa4 = patches.FancyArrowPatch((-3, -0.4), (3, -0.4), connectionstyle="arc3, rad=-.15", color="orange", arrowstyle="simple, head_width=5, head_length=10")


ax1.add_patch(e1)
ax1.add_patch(c1)
ax1.add_patch(e2)
ax1.add_patch(c2)
ax1.add_patch(fa1)
ax1.add_patch(fa2)
ax1.add_patch(fa3)
ax1.add_patch(fa4)



#Add text
ax1.text(-3, 1.5, r"$X$", color="k")
ax1.text(3, 1.5, r"$Y$", color="k")
ax1.text(-2.8, 0, r"$x_0$", color="b")
ax1.text(3.2, 0, r"$f(x_0)$", color="b")
ax1.text(-3, -.2, r"$\delta$", color="g")
ax1.text(3, -.2, r"$\epsilon$", color="r")
ax1.text(0, 1, r"$f$", color="orange")


plt.tight_layout()
plt.show()