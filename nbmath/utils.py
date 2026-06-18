import math
def diff(fx: list): #求导
    n = len(fx)
    if n == 0:
        return float('nan')
    elif n == 1:
        return [0]
    return [fx[i] * (n - 1 - i) for i in range(n - 1)]
def polyfit(x: list, y: list): #多项式拟合
def polyfit(x, y):
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    n = len(x)
    V = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(x[i] ** j)   # V[i][j] = x_i^j
        V.append(row)
    A = [row[:] for row in V]  # 深拷贝
    b = y[:]
    for col in range(n):
        max_row = col
        for i in range(col + 1, n):
            if abs(A[i][col]) > abs(A[max_row][col]):
                max_row = i
        A[col], A[max_row] = A[max_row], A[col]
        
        pivot = A[col][col]
        if abs(pivot) < 1e-15:
            raise ValueError("Singular matrix (x values may be duplicate)")
        for i in range(col + 1, n):
            factor = A[i][col] / pivot
            for j in range(col, n):
                A[i][j] -= factor * A[col][j]
            b[i] -= factor * b[col]
    c = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = b[i]
        for j in range(i + 1, n):
            s -= A[i][j] * c[j]
        c[i] = s / A[i][i]
    return c
def polyval(f: list, x): #代入求值
    n = len(f)
    if n == 0:
        return float('nan')
    elif n == 1:
        return f[0]
    return sum(coef * x ** (n - 1 - i) for i, coef in enumerate(f))
def linspace(start, end, steps): #np.linspace的纯python实现
    if steps==0:
        return []
    elif steps==1:
        return [start]
    dx = (end-start)/steps
    result = []
    for i in range(steps+1):
        x = start+i*dx
        result.append(x)
    return result
def gcd(a: int, b: int): #最大公约数
    while b:
        a, b = b, a%b
    return abs(a)
def lcm(a: int, b: int): #最小公倍数
    return a*b/gcd(a, b)
def floor(x): #向下取整
    if x>=0:
        return int(x)
    return int(x)-1
def trunc(x): #截断取整
    return int(x)
def frac(x): #小数部分
    if x>=0:
        return x-int(x)
    return x-int(x)+1
def fac(x): #阶乘
    if x>0 and int(x)==x:
        result = 1
        for i in range(1, x+1):
            result*=i
        return result
    elif x==0:
        return 1
    elif x<0 and int(x)==x:
        return float('nan')
    return math.gamma(x+1)
def is_even(x: int): #偶数判断
    return x%2==0
def is_odd(x: int): #奇数判断
    return x%2==1
def zeros(m: int, n: int): #m行n列的全零矩阵
    if m<0 or n<0:
        raise ValueError("size of a matrix cannot be a negative number")
    if m==0:
        return []
    if m==1:
        return [0]*n
    mat = []
    for i in range(m):
        mat.append([0]*n)
    return mat
def ones(m: int, n: int): #m行n列的全一矩阵
    if m<0 or n<0:
        raise ValueError("size of a matrix cannot be a negative number")
    if m==0:
        return []
    if m==1:
        return [1]*n
    mat = []
    for i in range(m):
        mat.append([1]*n)
    return mat
def eye(n: int): #单位矩阵
    if n<0:
        raise ValueError("size of a matrix cannot be a negative number")
    if n==0:
        return []
    if n==1:
        return [1]
    mat = zeros(n, n)
    for i in range(n):
        mat[i][i] = 1
    return mat
def add_2d_to_1d(A: list, b: list): #矩阵加向量
    n = len(A[0])
    if n!=len(b):
        raise ValueError("length of two lists didn't matched")
    m = len(A)
    mat = zeros(m, n)
    for i in range(m):
        for j in range(n):
            mat[i][j] = A[i][j]+b[j]
    return mat
def sqrtdenest(a, b, c): #双层根号
    delta = a**2-b**2*c
    if math.sqrt(delta)!=int(math.sqrt(delta)):
        raise ValueError("cannot simplify this redical")
    x, y = (a+delta)/2, (a-delta)/2
    return f"sqrt({x})+sqrt({y})"
def ngrad(f, x, h=1e-6):
    grad = [0]*len(x)
    for i in range(len(x)):
        x1 = x.copy()
        x2 = x.copy()
        x1[i]+=h
        x2[i]-=h
        grad[i] = (f(x1)-f(x2))/(2*h)
    return grad
def zeros_like(x):
    if isinstance(x, list):
        return [zeros_like(item) for item in x]
    elif isinstance(x, tuple):
        return tuple(zeros_like(item) for item in x)
    elif isinstance(x, (int, float, complex)):
        return type(x)(0)
    else:
        raise TypeError(f"Unsupported type.")
