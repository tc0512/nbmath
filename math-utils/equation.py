from cmath import sqrt
I = 1j
def solve_linear_equation_in_one_unknown(a, b): #一元一次方程
    return float('nan') if a==0 else [-b/a]
def solve_quadratic_equation(a, b, c): #一元二次方程
    if a==0:
        return float('nan')
    x1 = (-b+sqrt(b**2-4*a*c))/2a
    x2 = (-b-sqrt(b**2-4*a*c))/2a
    return [x1, x2]
def solve_cubic_equation_in_one_unknown(a, b, c, d):#一元三次方程
    if a==0:
        return float('nan')
    return [-(-3*c/a + b**2/a**2)/(3*(sqrt(-4*(-3*c/a + b**2/a**2)**3 + (27*d/a - 9*b*c/a**2 + 2*b**3/a**3)**2)/2 + 27*d/(2*a) - 9*b*c/(2*a**2) + b**3/a**3)**(1/3)) - (sqrt(-4*(-3*c/a + b**2/a**2)**3 + (27*d/a - 9*b*c/a**2 + 2*b**3/a**3)**2)/2 + 27*d/(2*a) - 9*b*c/(2*a**2) + b**3/a**3)**(1/3)/3 - b/(3*a), -(-3*c/a + b**2/a**2)/(3*(-1/2 - sqrt(3)*I/2)*(sqrt(-4*(-3*c/a + b**2/a**2)**3 + (27*d/a - 9*b*c/a**2 + 2*b**3/a**3)**2)/2 + 27*d/(2*a) - 9*b*c/(2*a**2) + b**3/a**3)**(1/3)) - (-1/2 - sqrt(3)*I/2)*(sqrt(-4*(-3*c/a + b**2/a**2)**3 + (27*d/a - 9*b*c/a**2 + 2*b**3/a**3)**2)/2 + 27*d/(2*a) - 9*b*c/(2*a**2) + b**3/a**3)**(1/3)/3 - b/(3*a), -(-3*c/a + b**2/a**2)/(3*(-1/2 + sqrt(3)*I/2)*(sqrt(-4*(-3*c/a + b**2/a**2)**3 + (27*d/a - 9*b*c/a**2 + 2*b**3/a**3)**2)/2 + 27*d/(2*a) - 9*b*c/(2*a**2) + b**3/a**3)**(1/3)) - (-1/2 + sqrt(3)*I/2)*(sqrt(-4*(-3*c/a + b**2/a**2)**3 + (27*d/a - 9*b*c/a**2 + 2*b**3/a**3)**2)/2 + 27*d/(2*a) - 9*b*c/(2*a**2) + b**3/a**3)**(1/3)/3 - b/(3*a)]
