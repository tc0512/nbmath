from nbmath.plots import core as plt
def lorenz(t_max, dt):
    x = 0.1
    y = 0.1
    z = 0.1
    sigma = 10
    rou = 28
    beta = 8/3
    depth = int(t_max/dt)
    for i in range(depth):
        dx = sigma*(y-x)
        dy = x*(rou-z)-y
        dz = x*y-beta*z
        x += dt*dx
        y += dt*dy
        z += dt*dz
        plt.point(x, z, "purple", 2, "")
        percent = (i+1)/depth*100
        print(f"\rplotting...{percent:.2f}%", end="")
    print("\nOk,done.")
    plt.keep_window()
def main():
    plt.window(400, 500)
    plt.setax(-20, 0, 20, 50)
    lorenz(50, 0.01)
if __name__=="__main__":
    main()
