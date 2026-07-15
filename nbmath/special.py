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
def elliptic_integral(k):
    return math.pi/2*hyp_pfq([1/2, 1/2], [1], k**2)
