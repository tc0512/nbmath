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
    def __init__(self, p1, p2): #p1,p2均为Point几何对象
        self.p1 = p1
        self.p2 = p2
    def length(self): #长度
        return dist(self.p1, self.p2)
    def midpoint(self): #中点
        return Point((self.p1.x+self.p2.x)/2, (self.p1.y+self.p2.y)/2)
    def expression(self): #表达式
        if self.p2.x==self.p1.x:
            y_min = min(self.p1.y, self.p2.y)
            y_max = max(self.p1.y, self.p2.y)
            return f"x={self.p1.x}{{{y_min}≤y≤{y_max}}}"
        k = (self.p2.y-self.p1.y)/(self.p2.x-self.p1.x)
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
class Circle: #圆
    def __init__(self, O, r): #圆心是Point几何对象
        self.O = O
        self.r = r
    def area(self): #面积
        return math.pi*self.r**2
    def circumference(self): #周长
        return 2*math.pi*self.r
    def diameter(self): #直径
        return 2*self.r
    def contains(self, point): #是否在圆内
        return dist(self.O, point)<=self.r
    def expression(self): #表达式
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
class Polygon:
    def __init__(self, points): #points是Point几何对象
        self.points = points
    def area(self): #面积
        n = len(self.points) 
        if n<3:
            return 0
        s = 0
        for i in range(n):
            x1, y1 = self.points[i].x, self.points[i].y
            x2, y2 = self.points[(i+1)%n].x, self.points[(i+1)%n].y
            s+=x1*y2-x2*y1
        return abs(s)/2
    def circumference(self):
        n = len(self.points)
        if n<2:
            return 0
        elif n==2:
            return dist(self.points[0], self.points[1])
        C = 0
        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i+1)%n]
            C+=dist(p1, p2)
        return C
