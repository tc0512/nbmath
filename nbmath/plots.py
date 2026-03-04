import turtle as t
_length = _height = None
_llx = _lly = _urx = _ury = None
def window(length, height): #窗口(t.setup)
    global _length, _height
    _length, _height = length, height
    t.setup(length, height)
    t.hideturtle()
    t.speed(0)
    t.tracer(0)
    t.penup()
def setax(llx, lly, urx, ury): #设置坐标系范围(t.setworldcoordinates)
    global _llx, _lly, _urx , _ury
    _llx, _lly, _urx , _ury = llx, lly, urx, ury
    t.setworldcoordinates(llx, lly, urx, ury)
def drawaxhline(): #绘制坐标轴
    global _length, _height, _llx, _lly, _urx , _ury
    if None in (_length, _height):
        raise ValueError("please use 'window' first to create a window")
    elif None in (_llx, _lly, _urx , _ury):
        x_min, x_max = -_length/2, _length/2
        y_min, y_max = -_height/2, _height/2
    else:
        x_min, x_max = _llx, _urx
        y_min, y_max = _lly, _ury
    t.penup()
    t.goto(x_min, 0)
    t.pendown()
    t.goto(x_max, 0)
    t.penup()
    t.goto(0, y_min)
    t.pendown()
    t.goto(0, y_max)
    t.penup()
    t.update()
def point(x, y, color: str, size: int, label: str): #描点
    t.penup()
    t.goto(x, y)
    t.pencolor(color)
    t.dot(size)
    t.write(label)
    t.penup()
    t.update()
def line(x: list, y: list, color: str, linewidth: int): #绘制线段
    t.penup()
    t.goto(x[0], y[0])
    t.pendown()
    t.pencolor(color)
    t.pensize(linewidth)
    t.goto(x[1], y[1])
    t.pensize(1)
    t.update()
def plot_function(f, x_min, x_max, color: str, linewidth: int, steps: int): #函数图像y=f(x)
    t.penup()
    dx = (x_max-x_min)/steps
    for i in range(steps+1):
        x = x_min+i*dx
        y = f(x)
        t.goto(x, y)
        if i==0:
            t.pendown()
            t.pencolor(color)
            t.pensize(linewidth)
    t.penup()
    t.update()
def scatter(points: list, color: str): #散点图
    t.penup()
    t.pencolor(color)
    for i in points:
        t.goto(i)
        t.dot(5)
    t.update()
def keep_window():
    t.done()
