import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

plt.rcParams['text.usetex'] = True #using latex
mpl.rcParams.update({'font.size': 20}) #font size

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -1, 7, -1, 4

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


# Use tex in labels
    i.set_xticks([])
    #ax.set_xticklabels([])
    i.set_yticks([])

# Create 'x' and 'y' labels placed at the end of the axes
    if i == ax5:
        continue
    i.set_xlabel('$x$', labelpad=-24, x=1.03)
    i.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)

# Draw arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    i.plot((1), (0), marker='>', transform=i.get_yaxis_transform(), **arrow_fmt)
    i.plot((0), (1), marker='^', transform=i.get_xaxis_transform(), **arrow_fmt)





# Plot lines
#ax1.plot([1, 1], [1, 3], color='r', ls='--')
#ax1.plot([1, 5], [3, 3], color='r', ls='--')
#ax1.plot([5, 5], [1, 3], color='r', ls='--')
#ax1.plot([1, 5], [1, 1], color='r', ls='--')



# Create big Rectangles 
r1 = patches.Rectangle((1, 1), 4, 2, edgecolor=(1, 0, 0, 1), facecolor=(1, 0, 0, .2), ls='--')
r1_2 = patches.Rectangle((4, 2), .5, .5, edgecolor=(0, 0, 1, 1))

# Add the patch to the Axes
ax1.add_patch(r1)
ax1.add_patch(r1_2)

ax1.plot([4.25], [2.25], color="b", marker=".")

#Add text
ax1.text(3, 3.5, r"aperto", color="r")
ax1.text(5.5, 3, r"\begin{center} {rettangolo\\ privo\\  dei lati} \end{center}", color="r")


r2 = patches.Rectangle((1, 1), 4, 2, edgecolor=(1, 0, 0, 1), facecolor=(1, 0, 0, .2))
r2_2 = patches.Rectangle((4.75, 1.5), .5, .5, edgecolor=(0, 0, 1, 1), facecolor="none")

ax2.add_patch(r2)
ax2.add_patch(r2_2)

ax2.plot([5], [1.75], color="b", marker=".")

# Fill small areas
ax2.fill_between(x=[5, 5.25], y1=[1.5, 1.5], y2=[2, 2], color="b", alpha=.2)

ax2.text(3, 3.5, r"chiuso", color="r")
ax2.text(5.5, 3, r"\begin{center} {rettangolo\\ comprensivo\\  dei lati} \end{center}", color="r")


r3 = patches.Rectangle((1, 1), 4, 2, edgecolor=(1, 0, 0, 1), facecolor=(1, 1, 1, 1), ls='--')
r3_2 = patches.Rectangle((5.1, 1.5), .5, .5, edgecolor=(0, 0, 1, 1), facecolor="none")

ax3.fill_between(x=[xmin, xmax], y1=[ymin, ymin], y2=[ymax, ymax], color=(1, 0, 0, .2))

ax3.add_patch(r3)
ax3.add_patch(r3_2)

# Add arrows between graphs 
ax3.arrow(-1, 1.5, 1.7, 0, head_width=.1, color="r")

ax3.plot([5.35], [1.75], color="b", marker=".")

ax3.text(xmin, 1.1, r"\begin{center} {complementare\\ aperto} \end{center}", color="r")


r4 = patches.Rectangle((1, 1), 4, 2, edgecolor=(1, 0, 0, 1), facecolor=(1, 0, 0, .2), ls='--')
ax4.add_patch(r4)

ax4.plot([1, 5], [3, 3], color="r")
ax4.plot([5, 5], [1, 3], color="r")

r4_2 = patches.Rectangle((4-.25, 3-.25), .5, .5, edgecolor=(0, 0, 1, 1), facecolor="none")
ax4.add_patch(r4_2)
ax4.fill_between(x=[4-.25, 4+.25], y1=[3, 3], y2=[3.25, 3.25], color="b", alpha=.2)

ax4.plot([4], [3], color="b", marker=".")

ax4.text(5.5, 3, r"\begin{center} {non è aperto\\ nè chiuso} \end{center}", color="r")


ax5.spines['bottom'].set_visible(False)
ax5.spines['left'].set_visible(False)

ax5.arrow(xmin, 1.5, xmax-xmin, 0, color="r", head_width=.5, length_includes_head=True)
ax5.text(1, 2.5, r"\begin{center} {complementare\\non è aperto} \end{center}", color="r")


r6 = patches.Rectangle((1, 1), 4, 2, edgecolor=(1, 0, 0, 1), facecolor=(1, 1, 1, 1), ls='--')
r6_2 = patches.Rectangle((2-.25, 1-.25), .5, .5, edgecolor=(0, 0, 1, 1), facecolor="none")

ax6.fill_between(x=[xmin, xmax], y1=[ymin, ymin], y2=[ymax, ymax], color=(1, 0, 0, .2))

ax6.add_patch(r6)
ax6.add_patch(r6_2)

ax6.plot([1, 1], [1, 3], color="r")
ax6.plot([1, 5], [1, 1], color="r")

ax6.fill_between(x=[2-.25, 2+.25], y1=[1, 1], y2=[1.25, 1.25], color="b", alpha=.2)

ax6.plot([2], [1], color="b", marker=".")




plt.tight_layout()
plt.show()