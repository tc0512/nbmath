#!/usr/bin/env python3
from nbmath.plots import core as plt
from random import*
def barnsley(n):
    p = [1]+[2]*85+[3]*7+[4]*7
    x, y = 0, 0
    for i in range(n):
        plt.point(x, y, "green", 1, "")
        ind = randint(0, 99)
        if p[ind]==1:
            x, y = 0, 0.16*y
        elif p[ind]==2:
            x, y = 0.85*x+0.04*y, -0.04*x+0.85*y+1.6
        elif p[ind]==3:
            x, y = 0.2*x-0.26*y, 0.23*x+0.22*y+1.6
        elif p[ind]==4:
            x, y = -0.15*x+0.28*y, 0.26*x+0.24*y+0.44
        percent = (i+1)/n*100
        print(f"\rplotting...{i+1}/50000 {percent:.2f}%", end="")
    print("\nOk,done.")
    keep_window()
def main():
    plt.window(720, 1440)
    plt.setax(-2.5, 0, 2.5, 10)
    barnsley(50000)
if __name__=="__main__":
    main()
