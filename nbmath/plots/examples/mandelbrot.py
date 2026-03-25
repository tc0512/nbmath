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
    width, height = 800, 600
    xmin, xmax = -2.5, 1.5
    ymin, ymax = -1.5, 1.5
    plt.window(width, height)
    plt.setax(xmin, ymin, xmax, ymax)
    plt.drawaxhline()
    total = width * height
    points = []
    for i in range(height):
        for j in range(width):
            x = xmin + (xmax - xmin) * j / width
            y = ymin + (ymax - ymin) * i / height
            c = complex(x, y)
            iter_count = mandelbrot(c)
            if iter_count == 100:
                color = "black"
            else:
                brightness = int(255 * iter_count / 100)
                color = f"#{brightness:02x}{brightness:02x}{brightness:02x}"
            points.append((j, i))
            plt.point(j, i, color, 1, "")
            print(f"\rplotting...{i*width+j}/{total}", end="")
    print("Ok,done.")
    plt.keep_window()
if __name__ == "__main__":
    main()
