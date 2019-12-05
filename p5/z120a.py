from graphics import *

win = GraphWin("Triangle", 200, 200)
obj1 = Line(Point(100, 100), Point(150, 100))
obj2 = Line(Point(150, 100), Point(80, 170))
obj3 = Line(Point(80, 170), Point(100, 100))

obj1.draw(win)
obj2.draw(win)
obj3.draw(win)

win.getMouse()
win.close()