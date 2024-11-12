from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np 
#import matplotlib.patches as patches
import time


def Dtime(start):
    print("--- %s seconds ---" % (time.time() - start))

def plt_parameters():
    plt.rcParams['text.usetex'] = True #using latex
    params = {'font.size': 20, 'text.latex.preamble' : r"""
    \usepackage{amsmath} 
    \usepackage{amssymb}
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
    ax1.set_xticks([.66, 1])
    ax1.set_xticklabels([r"$x_0$",1])
    ax1.set_yticks([])
    ax1.set_yticklabels([])

def axis_label_color(ax1, color):
    ax1.tick_params(axis='x', colors=color)

def plot_curves(ax1): 
    x = np.arange(0, 1, .01)

    ax1.plot(x, fun1(x), color = "r")

    ax1.plot(x, fun3(x), color="b")
    ax1.plot(x, fun3(x) - .25, color="orange", linestyle="--")
    ax1.plot(x, fun3(x) + .25, color="orange", linestyle="--")

def fun1 (x):
    return 5 * np.array(x) * (np.array(x) - 0.8) ** 2 + 2

def fun3 (x):
    return 2 * np.array(x) * (np.array(x) - 1.5) ** 2 + 1.1332645

def plot_segments(ax1):
    ax1.plot([1,1], [0, fun1(1)], color="g", linestyle="--")
    ax1.plot([.66,.66], [0, fun1(.66)], color="g", linestyle="--")
    ax1.plot([.2,.2], [fun3(.2), fun3(.2) - .25], color="orange", linestyle="--")

def text(ax1):
    #Add text
    dist = .02
    ax1.text(1 + dist, fun1(1), r"$y=\varphi(x)$", color="r")
    ax1.text(1 + dist, fun3(1), r"$y=|f(x)|$", color="b")
    ax1.text(.2 + dist, fun3(.2) - 3 * dist, r"$\varepsilon$", color="orange")

def color_area(ax1):
    x = np.arange(0, 1, .01)
    sec = np.array([])
    for i in x:
        if (fun3(i) + .25) >= fun1(i):
            sec = np.append(np.array(sec), np.array([i]))
    ax1.fill_between(x=sec, y1=np.array(fun3(sec) + .25), y2=np.array(fun1(sec)), color="purple", alpha=.2)

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
    text(AX)
    color_area(AX)
    plt.tight_layout()
    save_file()
    plt.show()
