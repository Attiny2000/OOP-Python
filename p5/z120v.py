from graphics import *

win = GraphWin("Polygon", 200, 200)

obj1 = Line(Point(100, 100), Point(150, 100))
obj2 = Line(Point(150, 100), Point(170, 120))
obj3 = Line(Point(170, 120), Point(150, 140))
obj4 = Line(Point(150, 140), Point(100, 140))
obj5 = Line(Point(100, 140), Point(100, 100))

obj1.draw(win)
obj2.draw(win)
obj3.draw(win)
obj4.draw(win)
obj5.draw(win)

win.getMouse()
win.close()