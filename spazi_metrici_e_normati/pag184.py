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
xmin, xmax, ymin, ymax = -0.5, 1.5, -.1, 1

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

ax1.set_xticks([1])
ax1.set_xticklabels([1])
ax1.set_yticks([])
ax1.set_yticklabels([])



def fun1 (x):
    return np.array(x) * (np.array(x) - 0.8) ** 2

def fun2 (x):
    return 5 * np.array(x) * (np.array(x) - 0.75) ** 2

x = np.arange(0, 1, .01)

ax1.plot(x, fun1(x) + .25, color = "b")
ax1.plot(x, fun1(x) + .5, color = "r")
ax1.plot(x, fun1(x) + .75, color = "b")

ax1.plot(x, fun2(x) + 0.4, color="orange")


#Add text
ax1.text(1, fun1(1) + .25, r"$f(x) - \varepsilon$", color="b")
ax1.text(1, fun1(1) + .75, r"$f(x) + \varepsilon$", color="b")
ax1.text(1, fun2(1) + .35, r"$f_k, \qquad k > N $", color="orange")
ax1.text(0.75, -0.2, r"$x=[0,1]$", color="g")



plt.tight_layout()
plt.show()