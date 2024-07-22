import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from curlyBrace import curlyBrace

plt.rcParams['text.usetex'] = True #using latex
mpl.rcParams.update({'font.size': 20}) #font size

fig, (ax1, ax2) = plt.subplots(1, 2)

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -1, 4, -1, 3

# Set identical scales for both axes
ax1.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=1)
ax2.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=1)

# Set bottom and left spines as x and y axes of coordinate system
ax1.spines['bottom'].set_position('zero')
ax1.spines['left'].set_position('zero')

ax2.spines['bottom'].set_position('zero')
ax2.spines['left'].set_position('zero')

# Remove top and right spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Create 'x' and 'y' labels placed at the end of the axes
ax1.set_xlabel('$x$', labelpad=-24, x=1.03)
ax1.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)

ax2.set_xlabel('$x$', labelpad=-24, x=1.03)
ax2.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)

# Draw arrows
arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax1.plot((1), (0), marker='>', transform=ax1.get_yaxis_transform(), **arrow_fmt)
ax1.plot((0), (1), marker='^', transform=ax1.get_xaxis_transform(), **arrow_fmt)

ax2.plot((1), (0), marker='>', transform=ax2.get_yaxis_transform(), **arrow_fmt)
ax2.plot((0), (1), marker='^', transform=ax2.get_xaxis_transform(), **arrow_fmt)

# Plot lines
ax1.arrow(0, 0, 3, 2, color='b', length_includes_head=True, head_width=.1)
ax1.plot([3, 3], [0, 2], color='k', ls='--')


ax2.arrow(0, 0, 3, 2, color='b', length_includes_head=True, head_width=.1)
ax2.plot([3, 3], [0, 2], color='k', ls='--')


# Use tex in labels
ax1.set_xticks([])
#ax.set_xticklabels([])
ax1.set_yticks([])

ax2.set_xticks([])
ax2.set_yticks([])

#Add text
ax1.text(3.1, 2.1, r"$(x,y)$")

ax2.text(3.1, 2.1, r"$(x,y)$")
ax2.text(1, -1, r"$\parallel (x,y) \parallel _{1} = |x| + |y|$", color="g")


#Add braces
curlyBrace(fig, ax1, [3, 0], [0, 0], .05, bool_auto=False, str_text=r"$\parallel (x,y) \parallel _ {\infty} = |x|$", color='g', lw=1, int_line_num=1, fontdict={"color": "green"})

curlyBrace(fig, ax2, [3, 0], [0, 0], .05, bool_auto=False, str_text=r"$|x|$", color='r', lw=1, int_line_num=1, fontdict={"color": "r"})
curlyBrace(fig, ax2, [3, 2], [3, 0], .05, bool_auto=False, str_text=r"$|y|$", color='r', lw=1, int_line_num=1, fontdict={"color": "r"})
curlyBrace(fig, ax2, [0, 0], [3, 2], .05, bool_auto=False, str_text=r"$|(x,y)|$", color='b', lw=1, int_line_num=1, fontdict={"color": "b"})


plt.tight_layout()
plt.show()