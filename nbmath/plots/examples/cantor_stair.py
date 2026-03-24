#!/usr/bin/env python3
import math
from nbmath.plots import core as plt
def F(x, depth=20):
    if depth == 0:
        return x
    if x < 1/3:
        return 0.5 * F(3*x, depth-1)
    elif x <= 2/3:
        return 0.5
    else:
        return 0.5 + 0.5 * F(3*x - 2, depth-1)
def main():
    plt.window(720, 720)
    plt.setax(-0.5, -0.5, 1.5, 1.5)
    plt.drawaxhline()
    plt.plot_function(F, 0, 1, "blue", 2, 800)
    plt.keep_window()
if __name__ == "__main__":
    main()
