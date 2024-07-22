import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True #using latex
mpl.rcParams.update({'font.size': 20}) #font size

fig, ax1 = plt.subplots()

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -5, 5, -3, 3

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
r = 2.5
ax1.plot([-r, 0], [0, r], color="r")
ax1.plot([0, r], [r, 0], color="r")
ax1.plot([r, 0], [0, -r], color="r")
ax1.plot([0, -r], [-r, 0], color="r")

# Fill area
ax1.fill_between(x=[-r, 0], y1=[0, -r], y2=[0, r], color="r", alpha=.2 )
ax1.fill_between(x=[0, r], y1=[-r, 0], y2=[r, 0], color="r", alpha=.2 )


# Use tex in labels
ax1.set_xticks([])
#ax.set_xticklabels([])
ax1.set_yticks([])


#Add text
ax1.text(2.5, 2, r"$B_{r}^{1} (0,0)$", color="r")
ax1.text(r+.1, 0, r"$r$", color="r")
ax1.text(-r-.3, 0, r"$-r$", color="r")
ax1.text(0, r+.1, r"$r$", color="r")
ax1.text(0, -r-.2, r"$-r$", color="r")



plt.tight_layout()
plt.show()