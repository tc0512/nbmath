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
    plt.setax(-1.5, -1.5, 1.5, 1.5)
    plt.drawaxhline()
    ALPHA = 1
    BETA = 1
    A = 5
    B = 4
    DELTA = math.pi/2
    t = linspace(0, 2*math.pi, 5000)
    p = []
    for i in t:
        x = ALPHA*math.sin(A*i+DELTA)
        y = BETA*math.sin(B*i)
        p.append((x, y))
    plt.scatter(p, "green", 1)
    plt.keep_window()
if __name__ == "__main__":
    main()
