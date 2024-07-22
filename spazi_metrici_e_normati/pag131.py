import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True #using latex
mpl.rcParams.update({'font.size': 20}) #font size

fig, ax1 = plt.subplots()

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -1, 5, -.5, 3

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
ax1.arrow(2.6, 1.6, .7, .7, color="b", head_width=.05)

# Plot lines
ax1.plot([1, 4], [2, 1], color='k', marker="o")


# Use tex in labels
ax1.set_xticks([])
#ax.set_xticklabels([])
ax1.set_yticks([])


#Add text
ax1.text(1.1, 2.1, r"$(x_1,y_1)$")
ax1.text(4.1, 1.1, r"$(x_2,y_2)$")

ax1.text(3.1, 2.6, r"$d \left( (x_2,y_2), (x_1,y_1) \right)= \\ \qquad = \left( (x_2,y_2) - (x_1,y_1) \right)$", color="b")



plt.tight_layout()
plt.show()