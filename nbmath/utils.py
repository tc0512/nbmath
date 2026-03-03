import time
def diff(fx: list): #求导
    n = len(fx)
    if n == 0:
        return float('nan')
    elif n == 1:
        return [0]
    return [fx[i] * (n - 1 - i) for i in range(n - 1)]
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
def timer(func): #计时器
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} 耗时: {time.time()-start:.4f}秒")
        return result
    return wrapper
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
