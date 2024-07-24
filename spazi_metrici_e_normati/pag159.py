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
r1 = patches.Rectangle((1, 1), 4, 2, edgecolor=(1, 0, 0, 1), facecolor=(1, 0, 0, .2), ls='--')

# Add the patch to the Axes
ax1.add_patch(r1)


ax1.plot([1], [2], color="b", marker=".")
ax1.plot([2.5], [2], color="g", marker=".")

ax1.plot([1, 2.5], [2, 2], color="g", ls="--")

ax1.plot([1, 5], [3, 3], color="r")
ax1.plot([5, 5], [1, 3], color="r")


# Add text
ax1.text(4, 1.5, r"$A$", color="r")
ax1.text(1-.1, 2, r"$z$", color="b")
ax1.text(2.5, 2+.1, r"$x_k$", color="g")
ax1.text(3.5, .6-.1, r"lato $\notin A$", color="y")
ax1.text(4.2, 3.5, r"lato $\in A$", color="y")
ax1.text(5.6, 3, r"\begin{center} {$x_k \rightarrow z$\\ma $z \notin A$} \end{center}", color="g")
ax1.text(5.8, 2.5, r"\begin{center} {A non è\\chiuso} \end{center}")


# Fancy arrows
a1 = patches.FancyArrowPatch((3, 0.9), (3.5, .6), arrowstyle="fancy, head_length=5, head_width=5", connectionstyle="arc3,rad=.1", color="y")
a2 = patches.FancyArrowPatch((3.8, 3.1), (4.2, 3.5), arrowstyle="fancy, head_length=5, head_width=5", connectionstyle="arc3,rad=-.1", color="y")

ax1.add_patch(a1)
ax1.add_patch(a2)


plt.tight_layout()
plt.show()