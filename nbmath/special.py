import math
def pochhammer(x, n):
    res = 1
    for i in range(n):
        res*=x+i
    return res
def hyp_pfq(a: list, b: list, z):
    res = 0
    n = 0
    while True:
        u = 1
        for p in a:
            u*=pochhammer(p, n)
        v = 1
        for q in b:
            v*=pochhammer(q, n)
        term = u/v*z**n/math.factorial(n)
        if abs(term)<=1e-12:
            break
        res+=term
        n+=1
    return res
def gamma(z):
    return math.gamma(z)
def erf(x):
    return math.erf(x)
def erfc(x):
    return 1-erf(x)
def bessel(x, alpha):
    m = 0
    J = 0
    while True:
        term = (-1)**m/(math.factorial(m)*gamma(m+alpha+1))*(x/2)**(2*m+alpha)
        if abs(term)<=1e-12:
            break
        J+=term
        m+=1
    return J
def neumann(x, alpha: float):
    return (bessel(x, alpha)*math.cos(alpha*math.pi)-bessel(x, -alpha))/math.sin(alpha*pi)
def beta(x, y):
    return gamma(x)*gamma(y)/gamma(x+y)
def first_elliptic_integral(k):
    return math.pi/2*hyp_pfq([1/2, 1/2], [1], k**2)
def second_elliptic_integral(k, dx=1e-6):
    total = 0
    x = 0
    while x<=math.pi/2:
        fx = math.sqrt(1-k**2*math.sin(x)**2)
        total+=fx*dx
        x+=dx
    return total
def zeta(s, max_iter=100):
    if s==1:
        return float('inf')
    if s==-1:
        return -1/12
    return sum([1/(n**s) for n in range(max_iter)])
def lambertW(x, branch=0):
    if x == -1/e:
        return -1
    # 选初始值
    if branch == 0:
        w = max(-0.9, log(1+x))  # 保证 > -1
    else:
        w = min(-1.1, log(-x))   # 保证 < -1
    # 牛顿迭代
    for _ in range(20):
        if abs(w + 1) < 1e-15:   # 防分母为零
            w += 1e-12
        w = w - (w - x * exp(-w)) / (w + 1)
    return w
