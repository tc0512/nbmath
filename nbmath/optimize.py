import math
import random
from .utils import eye, ngrad
def brute(f, x_min, x_max, points: int): #咆哮算法
    """
    f：要求解的函数
    x_min：定义域最小
    x_max：定义域最大
    points：选取点数
    """
    results = []
    x = x_min
    step_length = (x_max-x_min)/points
    while x<=x_max:
        results.append(f(x))
        x+=step_length
    fun = min(results)
    ind = results.index(fun)
    x_opt = x_min+ind*step_length
    return {"x": x_opt, "fun": fun}
def golden_section(f, x_min, x_max, tol): #黄金分割法
    """
    f：要求解的函数
    x_min：猜测区间最小
    x_max：猜测区间最大
    tol：容差
    """
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
    return (f(x+H)+f(x-H)-2*f(x))/(H**2)
def newton(f, x0, tol, max_iter: int): #牛顿法
    """
    f：要求解的函数
    x0：初始猜测
    tol：容差
    max_iter：迭代次数
    """
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
    """
    f：要求解的函数
    x0：初始猜测
    lr：学习率，一般取0.06
    tol：容差
    max_iter：迭代次数
    """
    x = x0
    for i in range(max_iter):
        df = ndiff1(f, x)
        if abs(df)<tol:
            return {"x": x, "fun": f(x)}
        x = x - lr * df
    return {"x": x, "fun": f(x)}
def simulated_annealing(f, x_min, x_max, temp, cooling, steps, tol): #模拟退火
    """
    f：要求解的函数
    x_min：猜测区间最小
    x_max：猜测区间最大
    temp：“温度”，一般取100
    cooling：冷却系数，一般取0.95
    steps：每步迭代次数，一般取1000
    tol：容差
    """
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
from nbmath.utils import eye, ngrad
def vec_add_scaled(x, alpha, p):
    """
    返回 x + alpha * p
    x: 向量 (n)
    alpha: 标量
    p: 向量 (n)
    """
    if len(x) != len(p):
        raise ValueError("x and p must have the same length")
    return [x[i] + alpha * p[i] for i in range(len(x))]
def norm(x):
    """计算向量 L2 范数"""
    return sum(xi**2 for xi in x) ** 0.5
def mat_mul_vec(A, v):
    """矩阵 A (m×n) × 向量 v (n) → 向量 (m)"""
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]

def matmul(A, B):
    """矩阵 A (m×n) × 矩阵 B (n×p) → 矩阵 (m×p)"""
    m, n = len(A), len(A[0])
    p = len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(p)] for i in range(m)]
def outer(a, b):
    """向量 a (n) 和 b (m) 的外积 → 矩阵 (n×m)"""
    return [[ai * bj for bj in b] for ai in a]
def BFGS(f, x0, tol, max_iter, alpha_init, grad=None):
    """
    f: 目标函数
    x0: 初始点（list）
    grad: 梯度函数（可选，若为 None 则用数值梯度）
    tol: 收敛容差，一般取1e-6
    max_iter: 最大迭代次数，一般取1000
    alpha_init: 初始步长，一般取1
    """
    n = len(x0)
    x = x0[:]
    if grad is None:
        grad = lambda x: ngrad(f, x)
    H = eye(n)
    for i in range(max_iter):
        g = grad(x)
        g_norm = norm(g)
        if g_norm < tol:
            return {
                "x": x,
                "fun": f(x),
                "iter": i,
                "converged": True,
                "grad_norm": g_norm
            }
        p = mat_mul_vec(H, g)
        p = [-v for v in p]  # 取负
        alpha = alpha_init
        f_x = f(x)
        x_new = vec_add_scaled(x, alpha, p)
        c1 = 1e-4
        g_dot_p = sum(g[i] * p[i] for i in range(n))
        while f(x_new) > f_x + c1 * alpha * g_dot_p:
            alpha *= 0.5
            if alpha < 1e-12:
                break
            x_new = vec_add_scaled(x, alpha, p)
        if alpha < 1e-12:
            return {
                "x": x,
                "fun": f_x,
                "iter": i,
                "converged": False,
                "grad_norm": g_norm
            }
        x_new = vec_add_scaled(x, alpha, p)
        g_new = grad(x_new)
        s = [x_new[i] - x[i] for i in range(n)]
        y = [g_new[i] - g[i] for i in range(n)]
        ys = sum(y[i] * s[i] for i in range(n))
        if ys < 1e-14:
            H = eye(n)
            x = x_new
            continue
        rho = 1.0 / ys
        I = eye(n)
        s_yT = outer(s, y)      # s * y^T
        y_sT = outer(y, s)      # y * s^T
        s_sT = outer(s, s)      # s * s^T
        def mat_sub(A, B):
            return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        def mat_scalar_mul(c, A):
            return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        left = mat_sub(I, mat_scalar_mul(rho, s_yT))
        right = mat_sub(I, mat_scalar_mul(rho, y_sT))
        H1 = matmul(left, H)
        H2 = matmul(H1, right)
        H3 = mat_scalar_mul(rho, s_sT)
        def mat_add(A, B):
            return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        H = mat_add(H2, H3)
        x = x_new
    return {
        "x": x,
        "fun": f(x),
        "iter": max_iter,
        "converged": False,
        "grad_norm": norm(grad(x))
    }
OPTIONS = {
    "x_min": -10,
    "x_max": 10,
    "points": 1000000,
    "tol": 1e-7,
    "x0": 0,
    "max_iter": 550,
    "lr": 0.06,
    "temp": 1000,
    "cooling": 0.95,
    "steps": 1000,
    "alpha_int": 1
}
def minimize(fun, x0, method="BFGS", options=OPTIONS):
    if method=="Brute":
        f, x_min, x_max, points = f, options["x_min"], options["x_max"], options["points"]
        return brute(fun, x_min, x_max, steps)
    elif method=="Golden Section":
        f, x_min, x_max, tol = f, options["x_min"], options["x_max"], options["tol"]
        return golden_section(f, x_min, x_max, tol)
    elif method=="Newton":
        f, x0, tol, max_iter = f, options["x0"], options["tol"], options["max_iter"]
        return newton(f, x0, tol, max_iter)
    elif method=="gradient_descent"
        f, x0, lr, tol, max_iter = f, options["x0"], options["lr"], options["tol"], options["max_iter"]
