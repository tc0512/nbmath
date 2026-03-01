import turtle as t
_length = _height = None
_llx = _lly = _urx = _ury = None
def window(length, height): #窗口(t.setup)
    global _length, _height
    _length, _height = length, height
    t.setup(length, height)
    t.speed(0)
    t.tracer(0)
    t.penup()
def setax(llx, lly, urx, ury): #设置坐标系范围(t.setworldcoordinates)
    global _llx, _lly, _urx , _ury
    _llx, _lly, _urx , _ury = llx, lly, urx, ury
    t.setworldcoordinates(llx, lly, urx, ury)
def drawax():
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
