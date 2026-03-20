import math
def brute(f, x_min, x_max, steps: int):
    results = []
    x = x_min
    step_length = (x_max-x_min)/steps
    while x<=x_max:
        results.append(f(x))
        x+=step_length
    fun = min(results)
    ind = results.index(fun)
    return {"x": results[ind], "fun": fun}
def golden_section(f, x_min, x_max, tol):
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
