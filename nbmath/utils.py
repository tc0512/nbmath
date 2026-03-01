import time
def diff(fx: list): #求导
    if len(fx)==0:
        return float('nan')
    elif len(fx)==1:
        return 0
    n = len(fx)
    fx.reverse()
    fpx = []
    for i in range(n-1, 0, -1):
        fpx.append(i*fx[i])
    return fpx
def polyval(f: list, x): #代入求值
    if len(f)==0:
        return float('nan')
    elif len(f)==1:
        return f[0]
    fx = 0
    power = len(f)-1
    for i in f:
        fx+=i*x**power
        power-=1
    return fx
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
