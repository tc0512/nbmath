#!/usr/bin/env python3
import math
from nbmath.plots import core as plt
def F(x, a=0.5, b=3, depth=60):
    fun = 0
    for n in range(depth):
        fun+=a**n*math.cos(b**n*math.pi*x)
    return fun
def main():
    plt.window(720, 720)
    plt.setax(-2, -2, 2, 2)
    plt.drawaxhline()
    plt.fun(F, -2, 2, "blue", 2, 720)
    plt.keep_window()
if __name__=="__main__":
    main()
