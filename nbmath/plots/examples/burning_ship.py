from nbmath.plots import core as plt
def burning_ship(c, max_iter):
    z = 0
    for i in range(max_iter):
        if abs(z)>2:
            return i
        z = (abs(z.real) + 1j * abs(z.imag))**2 + c
    return max_iter
def main():
    plt.window(400, 400)
    plt.setax(-2.5, -2, 1.5, 1.5)
    total = 400*400
