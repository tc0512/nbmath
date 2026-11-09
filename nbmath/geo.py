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
        return [lim, float('inf')] if self.p2.x>self.p1.x else [float('-inf'), lim]
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
class Polygon: # 多边形
    def __init__(self, points): #points: list[Point]
        self.points = points
    def __repr__(self):
        return f"Polygon({self.points})"
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
    def segments(self):
        n = len(self.points)
        if n<2:
            return []
        elif n==2:
            return [Seg(self.points[0], self.points[1])]
        segs = []
        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i+1)%n]
            segs.append(Seg(p1, p2))
        return segs
def intersection(obj1, obj2):
    if isinstance(obj1, Seg):
        if isinstance(obj2, Seg) or isinstance(obj2, Ray): #线段交线段/射线
            A1, B1, C1 = obj1.equation()
            A2, B2, C2 = obj2.equation()
            if A1*B2==A2*B1:
                return []
            x = (B1*C2-B2*C1)/(A1*B2-A2*B1)
            y = (-A1*C2+A2*C1)/(A1*B2-A2*B1)
            min1, max1 = obj1.eqdomain()
            min2, max2 = obj2.eqdomain()
            return [Point(x, y)] if min1<=x<=max1 and min2<=x<=max2 else []
        if isinstance(obj2, Line): #线段交直线
            A1, B1, C1 = obj1.equation()
            A2, B2, C2 = obj2.equation()
            if A1*B2==A2*B1:
                return []
            x = (B1*C2-B2*C1)/(A1*B2-A2*B1)
            y =(-A1*C2+A2*C1)/(A1*B2-A2*B1)
            min1, max1 = obj1.eqdomain()
            return [Point(x, y)] if min1<=x<=max1 else []
        if isinstance(obj2, Circle): #线段交圆
            A1, B1, C1 = obj1.equation()
            A2, B2, C2, D2, E2, F2 = obj2.equation()
            delta = A1**2*E2**2-4*A1**2*F2-2*A1*B1*D2*E2+4*A1*C1*D2+B1**2*D2**2-4*B1**2*F2+4*B1*C1*E2-4*C1**2
            if delta<0 or A1==0:
                return []
            x1 = (-B1*(-A1*math.sqrt(delta)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2+2*B1**2))-C1)/A1
            y1 = -A1*math.sqrt(delta)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2+2*B1**2)
            x2 = (-B1*(A1*math.sqrt(delta)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2 + 2*B1**2))-C1)/A1
            y2 = A1*math.sqrt(A1**2*E2**2-4*A1**2*F2-2*A1*B1*D2*E2+4*A1*C1*D2+B1**2*D2**2-4*B1**2*F2+4*B1*C1*E2-4*C1**2)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2+2*B1**2)
            points = []
            xmin, xmax = obj1.eqdomain()
            if xmin<=x1<=xmax:
                points.append(Point(x1, y1))
            if xmin<=x2<=xmax:
                points.append(Point(x2, y2))
            if len(points)==2:
                if points[0]==points[1]:
                    points = [points[0]]
            return points
        if isinstance(obj2, Polygon): #线段交多边形
            segs = obj2.segments()
            A1, B1, C1 = obj1.equation()
            points = []
            for i in segs:
                A2, B2, C2 = i.equation()
                if A1*B2==A2*B1:
                    continue
                x = (B1*C2-B2*C1)/(A1*B2-A2*B1)
                y = (-A1*C2+A2*C1)/(A1*B2-A2*B1)
                min1, max1 = obj1.eqdomain()
                min2, max2 = i.equation()
                if min1<=x<=max1 and min2<=x<=max2:
                    points.append(Point(x, y))
            return points
    if isinstance(obj1, Ray):
        if isinstance(obj2, Seg) or isinstance(obj2, Ray): #射线交线段/射线
            A1, B1, C1 = obj1.equation()
            A2, B2, C2 = obj2.equation()
            if A1*B2==A2*B1:
                return []
            x = (B1*C2-B2*C1)/(A1*B2-A2*B1)
            y = (-A1*C2+A2*C1)/(A1*B2-A2*B1)
            min1, max1 = obj1.eqdomain()
            min2, max2 = obj2.eqdomain()
            return [Point(x, y)] if min1<=x<=max1 and min2<=x<=max2 else []
        if isinstance(obj2, Line): #射线交直线
            A1, B1, C1 = obj1.equation()
            A2, B2, C2 = obj2.equation()
            if A1*B2==A2*B1:
                return []
            x = (B1*C2-B2*C1)/(A1*B2-A2*B1)
            y =(-A1*C2+A2*C1)/(A1*B2-A2*B1)
            min1, max1 = obj1.eqdomain()
            return [Point(x, y)] if min1<=x<=max1 else []
        if isinstance(obj2, Circle): #射线交圆
            A1, B1, C1 = obj1.equation()
            A2, B2, C2, D2, E2, F2 = obj2.equation()
            delta = A1**2*E2**2-4*A1**2*F2-2*A1*B1*D2*E2+4*A1*C1*D2+B1**2*D2**2-4*B1**2*F2+4*B1*C1*E2-4*C1**2
            if delta<0 or A1==0:
                return []
            x1 = (-B1*(-A1*math.sqrt(delta)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2+2*B1**2))-C1)/A1
            y1 = -A1*math.sqrt(delta)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2+2*B1**2)
            x2 = (-B1*(A1*math.sqrt(delta)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2 + 2*B1**2))-C1)/A1
            y2 = A1*math.sqrt(A1**2*E2**2-4*A1**2*F2-2*A1*B1*D2*E2+4*A1*C1*D2+B1**2*D2**2-4*B1**2*F2+4*B1*C1*E2-4*C1**2)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2+2*B1**2)
            points = []
            xmin, xmax = obj1.eqdomain()
            if xmin<=x1<=xmax:
                points.append(Point(x1, y1))
            if xmin<=x2<=xmax:
                points.append(Point(x2, y2))
            if len(points)==2:
                if points[0]==points[1]:
                    points = [points[0]]
            return points
        if isinstance(obj2, Polygon): #射线交多边形
            segs = obj2.segments()
            A1, B1, C1 = obj1.equation()
            points = []
            for i in segs:
                A2, B2, C2 = i.equation()
                if A1*B2==A2*B1:
                    continue
                x = (B1*C2-B2*C1)/(A1*B2-A2*B1)
                y = (-A1*C2+A2*C1)/(A1*B2-A2*B1)
                min1, max1 = obj1.eqdomain()
                min2, max2 = i.equation()
                if min1<=x<=max1 and min2<=x<=max2:
                    points.append(Point(x, y))
            return points
    if isinstance(obj1, Line):
        if isinstance(obj2, Seg) or isinstance(obj2, Ray): #直线交线段/射线
            A1, B1, C1 = obj1.equation()
            A2, B2, C2 = obj2.equation()
            if A1*B2==A2*B1:
                return []
            x = (B1*C2-B2*C1)/(A1*B2-A2*B1)
            y = (-A1*C2+A2*C1)/(A1*B2-A2*B1)
            xmin, xmax = obj2.eqdomain()
            return [Point(x, y)] if xmin<=x<=xmax else []
        if isinstance(obj2, Line): #直线交直线
            A1, B1, C1 = obj1.equation()
            A2, B2, C2 = obj2.equation()
            if A1*B2==A2*B1:
                return []
            x = (B1*C2-B2*C1)/(A1*B2-A2*B1)
            y = (-A1*C2+A2*C1)/(A1*B2-A2*B1)
            return [Point(x, y)]
        if isinstance(obj2, Circle): #直线交圆
            A1, B1, C1 = obj1.equation()
            A2, B2, C2, D2, E2, F2 = obj2.equation()
            delta = A1**2*E2**2-4*A1**2*F2-2*A1*B1*D2*E2+4*A1*C1*D2+B1**2*D2**2-4*B1**2*F2+4*B1*C1*E2-4*C1**2
            if delta<0 or A1==0:
                return []
            x1 = (-B1*(-A1*math.sqrt(delta)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2+2*B1**2))-C1)/A1
            y1 = -A1*math.sqrt(delta)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2+2*B1**2)
            x2 = (-B1*(A1*math.sqrt(delta)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2 + 2*B1**2))-C1)/A1
            y2 = A1*math.sqrt(A1**2*E2**2-4*A1**2*F2-2*A1*B1*D2*E2+4*A1*C1*D2+B1**2*D2**2-4*B1**2*F2+4*B1*C1*E2-4*C1**2)/(2*A1**2+2*B1**2)-(A1**2*E2-A1*B1*D2+2*B1*C1)/(2*A1**2+2*B1**2)
            return [Point(x1, y1)] if x1==x2 and y1==y2 else [Point(x1, y1), Point(x2, y2)]
