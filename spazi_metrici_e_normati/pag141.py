import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['text.usetex'] = True #using latex
mpl.rcParams.update({'font.size': 20}) #font size

fig, ax1 = plt.subplots()

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -5, 5, -3, 3

# Set identical scales for both axes
ax1.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=1)

# Remove top and right spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)


# Plot lines
circle1 = plt.Circle((0, 0), 2.5, color='red', alpha=.2)
circumference1 = plt.Circle((0, 0), 2.5, color='red', fill=False)

circle2 = plt.Circle((0, 1.5), .95, color='white', alpha=.5)
circle3 = plt.Circle((0, 1.5), .95, color='y', alpha=.2)
circumference2 = plt.Circle((0, 1.5), .95, color='y', fill=False)

ax1.add_patch(circle1)
ax1.add_patch(circumference1)

#ax1.add_patch(circle2)
ax1.add_patch(circle3)
ax1.add_patch(circumference2)

ax1.plot([0, 2.5], [0, 0], color="b")
ax1.plot([0, 0], [1.5, 2.45], color="g")

# Fancy arrows
a1 = patches.FancyArrowPatch((-0.9, 0.9), (-3.45, -1.9), arrowstyle="fancy, head_length=5, head_width=5", connectionstyle="arc3,rad=.1", color="y")
a2 = patches.FancyArrowPatch((0.1, 2.05), (1.7, 2.65), arrowstyle="fancy, head_length=5, head_width=5", connectionstyle="arc3,rad=.2", color="g")
a3 = patches.FancyArrowPatch((1.75, 0.2), (3.1, .9), arrowstyle="fancy, head_length=5, head_width=5", connectionstyle="arc3,rad=-.1", color="b")

ax1.add_patch(a1)
ax1.add_patch(a2)
ax1.add_patch(a3)

# Use tex in labels
ax1.set_xticks([])
#ax.set_xticklabels([])
ax1.set_yticks([])


#Add text
ax1.text(0, 0.1, r"$x$", color="k")
ax1.text(0.1, 1.5, r"$y$", color="k")
ax1.text(2.4, -1.3, r"$B_r(x)$", color="r")

ax1.text(-3.75, -2.1, r"$B_{\overline{r}}(y)$", color="y")
ax1.text(1.7, 2.65, r"$\overline{r} = r - d(x,y)$", color="g")
ax1.text(3.1, .9, r"$r$", color="b")



plt.tight_layout()
plt.show()