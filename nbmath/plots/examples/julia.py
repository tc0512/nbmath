from nbmath.plots import core as plt
def julia(z, max_iter=100, c=-0.8+0.156j):
    for i in range(max_iter):
        if abs(z)>2:
            return i
        z = z*z+c
    return max_iter
def main():
    plt.window(720, 720)
    plt.setax(-2, -2, 2, 2)
    total = 720*720
    for i in range(720):
        for j in range(720):
            x = -2+(4*j)/720
            y = -2+(4*i)/720
            z = complex(x, y)
            iter_count = julia(z)
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
            plotted = i*720+j
            print(f"\rplotting...{plotted}/{total} {plotted/total*100:.2f}%", end="")
    print("\nOk,done.")
    plt.keep_window()
if __name__=="__main__":
    main()
