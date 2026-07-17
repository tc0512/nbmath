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
import math

def lambert_w(x, branch=0, max_iter=30, tol=1e-14):
    e = math.exp(1)
    one_over_e = 1.0 / e
    if x < -one_over_e:
        raise ValueError(f"x = {x} < -1/e，实数范围内无解")
    if x == -one_over_e:
        return -1.0
    if x == 0.0:
        return 0.0
    if branch == 0:
        # W_0 主分支: w >= -1
        if -one_over_e < x < -0.1:
            w = -1.0 + math.sqrt(2 * (e * x + 1))
        else:
            w = math.log(1.0 + x) if x > -0.5 else 0.0
        if w <= -1.0:
            w = -0.999
    elif branch == -1:
        if x >= 0:
            raise ValueError(f"W_{-1} 在 x >= 0 时无实数值")
        if x > -0.1:
            w = -math.log(-x) - math.log(-math.log(-x))
        else:
            w = -1.0 - math.sqrt(2 * (e * x + 1))
        if w >= -1.0:
            w = -1.001
    else:
        raise ValueError("branch only can equal 0 or -1")
    for i in range(max_iter):
        if abs(w + 1.0) < 1e-15:
            w += 1e-12
        ew = math.exp(w)
        f = w * ew - x
        df = ew * (w + 1.0)
        w_new = w - f / df
        if abs(w_new - w) < tol * abs(w_new):
            return w_new
        w = w_new
    return w
