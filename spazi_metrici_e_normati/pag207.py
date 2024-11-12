from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np 
import time

def Dtime(start):
    print("--- %s seconds ---" % (time.time() - start))

def plt_parameters():
    plt.rcParams['text.usetex'] = True #using latex
    params = {'font.size': 20, 'text.latex.preamble' : r"""
    \usepackage{amsmath} 
    \usepackage{amssymb}
    \usepackage{mathtools}
              
    \everymath{\displaystyle}
    """}
    #font size
    pyplot.rcParams.update(params)

def axis_limits(ax1, xmin, xmax, ymin, ymax):
    # Set identical scales for both axes
    ax1.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=1)

def set_position(ax1):
    # Set bottom and left spines as x and y axes of coordinate system
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['left'].set_position('zero')

def remove_axes(ax1):
    # Remove top and right spines
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

def x_y_axis_labels(ax1):
    # Create 'x' and 'y' labels placed at the end of the axes
    ax1.set_xlabel('$x$', labelpad=-24, x=1.03)
    ax1.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)

def x_y_arrows(ax1):
    # Draw arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax1.plot((1), (0), marker='>', transform=ax1.get_yaxis_transform(), **arrow_fmt)
    ax1.plot((0), (1), marker='^', transform=ax1.get_xaxis_transform(), **arrow_fmt)

def axis_label(ax1):
    ax1.set_xticks([-2.5, -2])
    ax1.set_xticklabels([r"$b$", r"$-2$"])
    ax1.set_yticks([])
    ax1.set_yticklabels([])

def axis_label_color(ax1, color):
    ax1.tick_params(axis='x', colors=color)

def plot_curves(ax1): 
    x1 = np.arange(-6, -2, .01)
 
    ax1.plot(x1, fun1(x1), color = "r")

def fun1 (x):
    return np.e ** x * 5

def plot_segments(ax1):
    ax1.plot([-2.5, -2.5], [-.25, 1], color="b", linestyle="--")
    ax1.plot([-2, -2], [-.25, 1], color="g", linestyle="--")

def plot_points(ax1):
    pass


def text(ax1):
    #Add text
    dist = .05
    ax1.text(-5.5 - dist, fun1(-4), r"$y=f_k(x)$", color="r")




def save_file():
    file_name = str(__file__)[0:-1] + "ng"
    plt.savefig(file_name)


if __name__ == "__main__":
    START = time.time()
    plt_parameters()
    FIG, AX = plt.subplots()
    XMIN, XMAX, YMIN, YMAX = -0.5, 1.5, -.1, 1
    #axis_limits(AX, XMIN, XMAX, YMIN, YMAX)
    set_position(AX)
    remove_axes(AX)
    x_y_arrows(AX)
    axis_label(AX)
    axis_label_color(AX, "g")
    Dtime(START)
    plot_curves(AX)
    plot_segments(AX)
    plot_points(AX)
    text(AX)
    plt.tight_layout()
    save_file()
    plt.show()
