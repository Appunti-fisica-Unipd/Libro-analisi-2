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
xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5

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


# Use tex in labels

ax1.set_xticks([])
ax1.set_xticklabels([])
ax1.set_yticks([])
ax1.set_yticklabels([])



c1 = patches.Circle([0, 0], 1, edgecolor=(1, 0, 0, 1), facecolor=(1, 1, 1, 1))

ax1.fill_between(x=[xmin, xmax], y1=[ymin, ymin], y2=[ymax, ymax], color=(0, 0, 1, .2))
ax1.add_patch(c1)



#Add text
ax1.text(np.sqrt(2)/2 +.1, -np.sqrt(2)/2 -.1, r"$B_R(0)$", color="r")
ax1.text(1.2, .5, r"$A$", color="b")


plt.tight_layout()
plt.show()