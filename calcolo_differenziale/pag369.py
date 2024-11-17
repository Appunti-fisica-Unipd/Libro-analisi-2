import matplotlib as mpl
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
    plt.rcParams.update(params)

def axis_limits(ax1, xmin, xmax, ymin, ymax):
    # Set identical scales for both axes
    ax1.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect=1)

def set_position(ax1):
    # Set bottom and left spines as x and y axes of coordinate system
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['left'].set_position('zero')

def remove_axes(ax1, *args):
    # Remove top and right spines
    if "n" in args or "N" in args: 
        ax1.spines['top'].set_visible(False)
    if "e" in args or "E" in args: 
        ax1.spines['right'].set_visible(False)
    if "s" in args or "S" in args: 
        ax1.spines['bottom'].set_visible(False)
    if "w" in args or "W" in args: 
        ax1.spines['left'].set_visible(False)

def x_y_axis_labels(ax1, args):
    # Create 'x' and 'y' labels placed at the end of the axes
    if "n" in args or "N" in args: 
        ax1.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)
    if "e" in args or "E" in args: 
        ax1.set_xlabel('$x$', labelpad=-24, x=1.03)
    if "s" in args or "S" in args: 
        pass
    if "w" in args or "W" in args: 
        pass
    
def axis_arrows(ax1, c, args):
    # Draw arrows
    arrow_fmt = dict(markersize=4, color=c, clip_on=False)
    if "n" in args or "N" in args: 
        ax1.plot((0), (1), marker='^', transform=ax1.get_xaxis_transform(), **arrow_fmt)
    if "e" in args or "E" in args: 
        ax1.plot((1), (0), marker='>', transform=ax1.get_yaxis_transform(), **arrow_fmt)
    if "s" in args or "S" in args: 
        pass
    if "w" in args or "W" in args: 
        pass

def axis_label(ax1, xtic, xlab, ytic, ylab):
    ax1.set_xticks(xtic)
    ax1.set_xticklabels(xlab)
    ax1.set_yticks(ytic)
    ax1.set_yticklabels(ylab)

def x_label_color(ax1, color):
    ax1.tick_params(axis='x', colors=color)

def y_label_color(ax1, color):
    ax1.tick_params(axis='y', colors=color)

def fun(x):
    return -(x - 2) ** 2 + 3

def fun2(x):
    return (x - 2) ** 2 + 2

def plot_curves(ax1): 
    x = np.arange(1, 3, .01)
    ax1.plot(x, fun(x), color="r")
    pass

def plot_curves2(ax1):
    x = np.arange(1, 3, .01)
    ax1.plot(x, fun2(x), color="r")
    pass

def plot_segments(ax1):
    ax1.plot([0, 1/4], [0, 4], color="r")
    ax1.plot([1/4, 1/2], [4, 0], color="r")
    ax1.plot([1/2, 1], [0, 0], color="r")
    ax1.plot([0, 1/4], [4, 4], color="r", linestyle="--")

def plot_points(ax1):
    pass


def text(ax1, coor, text, c):
    #Add text
    ax1.text(coor[0], coor[1], text, color=c)


def save_file():
    file_name = str(__file__)[0:-1] + "ng"
    plt.savefig(file_name)


if __name__ == "__main__":
    START = time.time()
    plt_parameters()
    FIG, [AX, AX2] = plt.subplots(ncols=2)
    axis_limits(AX, -.2, 4, -.1, 4)
    axis_limits(AX2, -.2, 4, -.1, 4)

    set_position(AX)
    set_position(AX2)
    remove_axes(AX, "n", "e")
    remove_axes(AX2, "n", "e")
    axis_arrows(AX, "k", ["n", "e"])
    axis_arrows(AX2, "k", ["n","e"])
    axis_label(AX, xtic=[2], xlab=[r"$x_0$"], ytic=[], ylab=[])
    axis_label(AX2, xtic=[2], xlab=[r"$x_0$"], ytic=[], ylab=[])
    x_label_color(AX, color="teal")
    x_label_color(AX2, color="teal")

    plot_curves(AX)
    plot_curves2(AX2)

    AX.title.set_text(r"$f^{\prime\prime}(x_0)<0$")
    AX2.title.set_text(r"$f^{\prime\prime}(x_0)>0$")

    plt.tight_layout()
    save_file()
    Dtime(START)
    plt.show()

