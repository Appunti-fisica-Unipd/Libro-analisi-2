import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 

plt.rcParams['text.usetex'] = True #using latex
mpl.rcParams.update({'font.size': 20}) #font size

fig, ax1 = plt.subplots()

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -.1, 2.1, -.1, 2.1

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


# Plot lines
ax1.plot([0, 1/8], [0,2], color="r")
ax1.plot([1/8, 1/4], [2,0], color="r")
ax1.plot([1/4, 1], [0, 0], color="r")
ax1.plot([0, 1/8], [2, 2], color="r", ls="--")


# Use tex in labels
ax1.set_xticks([1/4, 1])
ax1.set_xticklabels([r"$\frac{1}{2^n}$", r"$1$"])
ax1.set_yticks([2])
ax1.set_yticklabels([r"$n$"])

# Fill area
ax1.fill_between(x=[0, 1/8-.005], y1=[0, 2], color='c', alpha=.2)
ax1.fill_between(x=[1/8, 1/4], y1=[2, 0], color='c', alpha=.2)




#Add text
ax1.text(1/4, 1, r"$y=g_n(x)$", color="r")






plt.tight_layout()
plt.show()