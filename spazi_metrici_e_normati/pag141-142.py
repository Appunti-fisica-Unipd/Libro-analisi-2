import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from curlyBrace import curlyBrace

plt.rcParams['text.usetex'] = True #using latex
mpl.rcParams.update({'font.size': 20}) #font size

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -1, 6, -1, 4

graphes = [ax1, ax2, ax3, ax4, ax5, ax6]

for i in graphes:
# Set identical scales for both axes
    i.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=1)

# Set bottom and left spines as x and y axes of coordinate system
    i.spines['bottom'].set_position('zero')
    i.spines['left'].set_position('zero')

# Remove top and right spines
    i.spines['top'].set_visible(False)
    i.spines['right'].set_visible(False)


# Create 'x' and 'y' labels placed at the end of the axes
    i.set_xlabel('$x$', labelpad=-24, x=1.03)
    i.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)

# Draw arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    i.plot((1), (0), marker='>', transform=i.get_yaxis_transform(), **arrow_fmt)
    i.plot((0), (1), marker='^', transform=i.get_xaxis_transform(), **arrow_fmt)

# Use tex in labels
    i.set_xticks([])
    #ax.set_xticklabels([])
    i.set_yticks([])



# Plot lines
ax1.plot([1, 1], [1, 3], color='r', ls='--')
ax1.plot([1, 5], [3, 3], color='r', ls='--')
ax1.plot([5, 5], [1, 3], color='r', ls='--')
ax1.plot([1, 5], [1, 1], color='r', ls='--')





ax2.arrow(0, 0, 3, 2, color='b', length_includes_head=True, head_width=.1)
ax2.plot([3, 3], [0, 2], color='k', ls='--')


# Fill areas
ax1.fill_between(x=[1, 5], y1=[1, 1], y2=[3, 3], color="r", alpha=.2)



#Add text
#ax1.text(3.1, 2.1, r"$(x,y)$")

#ax2.text(3.1, 2.1, r"$(x,y)$")
#ax2.text(1, -1, r"$\parallel (x,y) \parallel _{1} = |x| + |y|$", color="g")




plt.tight_layout()
plt.show()