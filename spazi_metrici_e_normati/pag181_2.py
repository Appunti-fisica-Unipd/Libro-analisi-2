from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.patches as patches
import matplotlib as mpl


plt.rcParams['text.usetex'] = True #using latex
params = {'font.size': 20, 'text.latex.preamble' : r"\usepackage{amsmath} \usepackage{amssymb}"}
#font size
pyplot.rcParams.update(params)


fig, ax1 = plt.subplots()

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -5, 5, -.1, 3

# Set identical scales for both axes
ax1.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=1)

# Set bottom and left spines as x and y axes of coordinate system
ax1.spines['bottom'].set_position('zero')
ax1.spines['left'].set_position('zero')

# Remove top and right spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Create 'x' and 'y' labels placed at the end of the axes
#ax1.set_xlabel('$x$', labelpad=-24, x=1.03)
#ax1.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)

# Draw arrows
arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax1.plot((1), (0), marker='>', transform=ax1.get_yaxis_transform(), **arrow_fmt)
ax1.plot((0), (1), marker='^', transform=ax1.get_xaxis_transform(), **arrow_fmt)


# Use tex in labels

ax1.set_xticks([])
ax1.set_xticklabels([])
ax1.set_yticks([])
ax1.set_yticklabels([])


ax1.fill_between(x=[xmin, 0], y1=[0, 0], y2=[ymax, ymax], color = (1, 0, 0, .2))
ax1.fill_between(x=[0, xmax], y1=[2, 2], y2=[ymax, ymax], color = (1, 0, 0, .2))

ax1.plot([xmin, 0], [0, 0], color = (0, 0, 1, 1))
ax1.plot([0, xmax], [2, 2], color = (0, 0, 1, 1))
ax1.scatter(0, 2, marker='x', color=(0, 0, 1, 1))
ax1.scatter(0, 0, marker='o', color=(0, 0, 1, 1))




with mpl.rc_context({"path.sketch":(5, 30, 1)}):
    ax1.plot([0, 0], [0, 2], color = (1, 0, 0, 1))
    ax1.plot([0, xmax], [2, 2], color = (1, 0, 0, 1))
    ax1.plot([xmin, 0], [0, 0], color = (1, 0, 0, 1))




#Add text
ax1.text(-.2, 2, r"$1$", color="b")
ax1.text(-4.8, 2.4, r"""$C = \{ (x,y) \in \mathbb{R}^{2} \; \big| \; y \geq f(x) \}$ 
                        $C $ è chiuso""", color="r")

plt.tight_layout()
plt.show()