#!/usr/bin/env python3
import sys
import math
from nbmath.plots import core as plt
def mandelbrot(c, max_iter=100):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter
def main():
    width, height = 400, 300
    xmin, xmax = -2.5, 1.5
    ymin, ymax = -1.5, 1.5
    plt.window(width, height)
    plt.setax(xmin, ymin, xmax, ymax)
    total = width * height
    for i in range(height):
        for j in range(width):
            x = xmin + (xmax - xmin) * j / width
            y = ymin + (ymax - ymin) * i / height
            c = complex(x, y)
            iter_count = mandelbrot(c)
            if iter_count==100:
                color = "black"
            elif iter_count<=25:
                color = "red"
            elif iter_count<=50:
                color = "orange"
            elif iter_count<=75:
                color = "yellow"
            elif iter_count<=99:
                color = "aqua"
            plt.point(x, y, color, 1, "")
            plotted = i*width+j
            print(f"\rplotting...{plotted}/{total} {plotted/total*100:.2f}%", end="")
    print("\nOk,done.")
    plt.keep_window()
if __name__ == "__main__":
    main()
