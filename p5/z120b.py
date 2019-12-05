from graphics import *

win = GraphWin("Sqare", 200, 200)
obj = Rectangle(Point(80, 80), Point(170, 150))

obj.draw(win)
win.getMouse()
win.close()