from nbmath.plots import core as plt
def newton(c, max_iter):
    z = c
    roots = [complex(1, 0), 
             complex(-0.5, 0.866), 
             complex(-0.5, -0.866)]
    
    for i in range(max_iter):
        try:
            z = z - (z**3 - 1) / (3 * z**2)
        except ZeroDivisionError:
            return i, 0
        for idx, root in enumerate(roots):
            if abs(z - root) < 1e-6:
                return i, idx
    return max_iter, 3
def main():
    plt.window(400, 400)
    plt.setax(-2, -2, 2, 2)
    total = 400*400
    for i in range(400):
        y = -2 + (4 * i) / 400
        for j in range(400):
            x = -2 + (4 * j) / 400
            c = complex(x, y)
            iter_count, root = newton(c, 50)
            colors = ["red", "green", "blue", "black"]
            color = colors[root] if root < 3 else "white"
            plotted = i*400+j+1
            plt.point(x, y, color, 1, "")
            print(f"\rplotting...{plotted}/{total} {plotted/total*100:.2f}%", end="")
    print("\nOK,done.")
    plt.keep_window()
if __name__ == "__main__":
    main()
