from nbmath.plots import core as plt
def burning_ship(c, max_iter=100):
    z = 0
    for i in range(max_iter):
        if abs(z)>2:
            return i
        z = (abs(z.real) + 1j * abs(z.imag))**2 + c
    return max_iter
def main():
    plt.window(400, 400)
    plt.setax(-2, -2, 2, 2)
    total = 400*400
    for i in range(400):
        for j in range(400):
            x = -2+(4*j)/400
            y = -2+(4*i)/400
            c = complex(x, y)
            iter_count = burning_ship(c)
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
            plotted = i*400+j+1
            print(f"\rplotting...{plotted}/{total} {plotted/total*100:.2f}%", end="")
    print("\nOk,done.")
    plt.keep_window()
if __name__=="__main__":
    main()
