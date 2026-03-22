#!/usr/bin/env python3
import math
from nbmath.plots import core as plt
def main():
    plt.window(800, 600)
    plt.setax(-2*math.pi, -1.5*math.pi, 2*math.pi, 1.5*math.pi)
    plt.drawaxhline()
    plt.plot_function(lambda x:math.sin(x), -2*math.pi, 2*math.pi, "blue", 2, 800)
    plt.keep_window()
if __name__ == "__main__":
    main()
