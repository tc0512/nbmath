#!/usr/bin/env python3
import math
from nbmath.plots import core as plt
def linspace(start, end, steps):
    if steps==0:
        return []
    elif steps==1:
        return [start]
    dx = (end-start)/steps
    result = []
    for i in range(steps+1):
        x = start+i*dx
        result.append(x)
    return result
def main():
    plt.window(720, 720)
    plt.setax(-3, -3, 3, 3)
    plt.drawaxhline()
    A = 1
    theta = linspace(-2*math.pi, 2*math.pi, 2000)
    p = []
    for i in theta:
        r = A*(1-math.cos(i))
        x = r*math.cos(i)
        y = r*math.sin(i)
        p.append((x, y))
    plt.scatter(p, "red", 2)
    plt.keep_window()
if __name__ == "__main__":
    main()
