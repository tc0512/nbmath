import math
class Point: #点
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
def dist(p1: Point, p2: Point): #两点距离
    return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
class Seg: #线段
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"
    def length(self): #长度
        return dist(self.p1, self.p2)
    def midpoint(self): #中点
        return Point((self.p1.x+self.p2.x)/2, (self.p1.y+self.p2.y)/2)
    def equation(self): #表达式
        A = self.p1.y-self.p2.y
        B = self.p2.x-self.p1.x
        C = self.p1.x*self.p2.y-self.p2.x*self.p1.y
        return [A, B, C]
    def eqdomain(self): #表达式定义域
        s = min(self.p1.x, self.p2.x)
        f = max(self.p1.x, self.p2.x)
        return [s, f]
class Ray: #射线
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    def __repr__(self):
        return f"Ray({self.p1}, {self.p2})"
    def equation(self): #表达式
        A = self.p1.y-self.p2.y
        B = self.p2.x-self.p1.x
        C = self.p1.x*self.p2.y-self.p2.x*self.p1.y
        return [A, B, C]
    def eqdomain(self): #表达式定义域
        lim = self.p1.x
        return [lim, ">="] if self.p2.x>self.p1.x else [lim, "<="] #[极值, 符号]
class Line: #直线
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"
    def equation(self): #表达式
        A = self.p1.y-self.p2.y
        B = self.p2.x-self.p1.x
        C = self.p1.x*self.p2.y-self.p2.x*self.p1.y
        return [A, B, C]
class Circle: #圆
    def __init__(self, O: Point, r):
        self.O = O
        self.r = r
    def __repr__(self):
        return f"Circle({self.O}, {self.r})"
    def area(self): #面积
        return math.pi*self.r**2
    def circumference(self): #周长
        return 2*math.pi*self.r
    def diameter(self): #直径
        return 2*self.r
    def contains(self, point: Point): #是否在圆内
        return dist(self.O, point)<=self.r
    def equation(self): #表达式
        A = 1
        B = 0
        C = 1
        D = -2*self.O.x
        E = -2*self.O.y
        F = self.O.x**2+self.O.y**2-self.r**2
        return [A, B, C, D, E, F]
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
