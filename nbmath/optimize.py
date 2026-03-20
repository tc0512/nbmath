import math
import random
def brute(f, x_min, x_max, steps: int): #咆哮算法
    results = []
    x = x_min
    step_length = (x_max-x_min)/steps
    while x<=x_max:
        results.append(f(x))
        x+=step_length
    fun = min(results)
    ind = results.index(fun)
    return {"x": results[ind], "fun": fun}
def golden_section(f, x_min, x_max, tol): #黄金分割法
    phi = (math.sqrt(5)-1)/2
    x1 = x_max-phi*(x_max-x_min)
    x2 = x_min+phi*(x_max-x_min)
    while abs(x_max-x_min)>tol:
        if f(x1)<f(x2):
            x_max = x2
            x2 = x1
            x1 = x_max-phi*(x_max-x_min)
        else:
            x_min = x1
            x1 = x2
            x2 = x_min+phi*(x_max-x_min)
    x = (x_min+x_max)/2
    fun = f(x)
    return {"x": x, "fun": fun}
def ndiff1(f, x): #数值导
    H = 1e-6
    return (f(x+H)-f(x-H))/(2*H)
def ndiff2(f, x): #数值二阶导
    H = 1e-4
    return (f(x+H)-f(x-H)-2*f(x))/(H**2)
def newton(f, x0, tol, max_iter: int): #牛顿法
    x = x0
    for i in range(max_iter):
        df = ndiff1(f, x)
        d2f = ndiff2(f, x)
        if abs(df) < tol:
            return {"x": x, "fun": f(x)}
        if df==0:
            raise ZeroDivisionError("cannot divide by zero")
        if d2f==0:
            raise ZeroDivisionError("cannot divide by zero")
        x = x - df / d2f
    return {"x": x, "fun": f(x)}
def gradient_descent(f, x0, lr, tol, max_iter: int): #梯度下降
    x = x0
    for i in range(max_iter):
        df = ndiff(f, x)
        if abs(df)<tol:
            return {"x": x, "fun": f(x)}
        x = x - lr * df
    return {"x": x, "fun": f(x)}
def simulated_annealing(f, x_min, x_max, temp, cooling, steps, tol): #模拟退火
    x = random.uniform(x_min, x_max)
    fx = f(x)
    best_x, best_f = x, fx
    for step in range(steps):
        T = temp * (cooling ** step)
        if T < 1e-3:
            break
        x_new = x + random.uniform(-1, 1) * (x_max - x_min) * 0.1
        x_new = max(x_min, min(x_max, x_new))
        f_new = f(x_new)
        if f_new < fx:
            x, fx = x_new, f_new
            if fx<best_f:
                best_x, best_f = x, fx
        else:
            delta = f_new-fx
            p = math.exp(-delta/T)
            if random.random()<p:
                x, fx = x_new, f_new
    return {"x": best_x, "fun": best_f}
