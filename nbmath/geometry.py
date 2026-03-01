import math
class Point: #点
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def expression(self): #表达式
        return f"({self.x}, {self.y})"
def dist(p1, p2): #两点距离
    return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
class Line: #线段
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def length(self): #长度
        return dist(self.p1, self.p2)
    def midpoint(self): #中点
        return Point((self.p1.x+self.p2.x)/2, (self.p1.y+self.p2.y)/2)
    def expression(self): #表达式
        k = (self.p2.y-self.p1.y)/(self.p2.x-self.p1.y)
        b = self.p1.y-k*self.p1.x
        x_min = min(self.p1.x, self.p2.x)
        x_max = max(self.p1.x, self.p2.x)
        if k!=0:
            if b>0:
                return f"y={k}x+{b}{{{x_min}≤x≤{x_max}}}"
            elif b==0:
                return f"y={k}x{{{x_min}≤x≤{x_max}}}"
            elif b<0:
                return f"y={k}x-{-b}{{{x_min}≤x≤{x_max}}}"
        else:
            return f"y={b}{{{x_min}≤x≤{x_max}}}"
class Circle:
    def __init__(self, O, r):
        self.O = O
        self.r = r
    def area(self):
        return math.pi*self.r**2
    def circumference(self):
        return 2*math.pi*self.r
    def diameter(self):
        return 2*self.r
    def contains(self, point):
        return dist(self.O, point)<=self.r
    def expression(self):
        a = self.O.x
        b = self.O.y
        if a>0:
            if b>0:
                return f"(x-{a})^2+(y-{b})^2={self.r**2}"
            elif b==0:
                return f"(x-{a})^2+y^2={self.r**2}"
            elif b<0:
                return f"(x-{a})^2+(y+{-b})^2={self.r**2}"
        elif a==0:
            if b>0:
                return f"x^2+(y-{b})^2={self.r**2}"
            elif b==0:
                return f"x^2+y^2={self.r**2}"
            elif b<0:
                return f"x^2+(y+{-b})^2={self.r**2}"
        elif a<0:
            if b>0:
                return f"(x+{-a})^2+(y-{b})^2={self.r**2}"
            elif b==0:
                return f"(x+{-a})^2+y^2={self.r**2}"
            elif b<0:
                return f"(x+{-a})^2+(y+{-b})^2={self.r**2}"
