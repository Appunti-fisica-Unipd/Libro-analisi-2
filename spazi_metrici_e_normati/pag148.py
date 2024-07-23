import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

plt.rcParams['text.usetex'] = True #using latex
mpl.rcParams.update({'font.size': 20}) #font size

fig, ax1, = plt.subplots()

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -1, 7, -1, 4


# Set identical scales for both axes
ax1.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=1)

# Set bottom and left spines as x and y axes of coordinate system
ax1.spines['bottom'].set_position('zero')
ax1.spines['left'].set_position('zero')

# Remove top and right spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)


# Use tex in labels
ax1.set_xticks([])
#ax.set_xticklabels([])
ax1.set_yticks([])

# Create 'x' and 'y' labels placed at the end of the axes
ax1.set_xlabel('$x$', labelpad=-24, x=1.03)
ax1.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)

# Draw arrows
arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax1.plot((1), (0), marker='>', transform=ax1.get_yaxis_transform(), **arrow_fmt)
ax1.plot((0), (1), marker='^', transform=ax1.get_xaxis_transform(), **arrow_fmt)



# Create big Rectangles 
r1 = patches.Rectangle((1, 1), 4, 2, edgecolor=(0, 0, 1, 1), facecolor=(1, 0, 0, .2), ls='--')
r1_2 = patches.Rectangle((3-.25, 1-.25), .5, .5, edgecolor="c", facecolor="none")
r1_3 = patches.Rectangle((4-.25, 3-.25), .5, .5, edgecolor="c", facecolor="none")


# Add the patch to the Axes
ax1.add_patch(r1)
ax1.add_patch(r1_2)
ax1.add_patch(r1_3)


ax1.plot([3], [1], color="c", marker=".")
ax1.plot([4], [3], color="c", marker=".")


ax1.plot([1, 5], [3, 3], color="b")
ax1.plot([5, 5], [1, 3], color="b")


#Add text
ax1.text(3, 2, r"$A$", color="r")
ax1.text(5.5, 3, r"$\partial A$", color="b")


plt.tight_layout()
plt.show()