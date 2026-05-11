import random
import nbmath.plots as plt
import math

def random_walk(steps=1000, step_size=1):
    x, y = 0, 0
    xs, ys = [x], [y]
    for _ in range(steps):
        angle = random.uniform(0, 2*math.pi)
        x+=step_size*math.cos(angle)
        y+=step_size*math.sin(angle)
        xs.append(x)
        ys.append(y)
    return xs, ys
def main():
    xs, ys = random_walk(2000)
    plt.window(720, 720)
    plt.setax(-50, -50, 50, 50)
    for i in range(len(xs)):
        plt.point(xs[i], ys[i], "blue", 1, "")
        percent = i/2000*100
        print(f"\rplotting...{i}/2000 {percent:.2f}%", end="")
    print("\nOk,done.")
    plt.keep_window()
if __name__=="__main__":
    main()
