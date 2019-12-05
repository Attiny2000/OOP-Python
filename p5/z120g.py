from graphics import *

win = GraphWin("Polygon", 200, 200)

obj = Polygon(Point(120, 100), Point(140, 120), Point(140, 140), Point(120, 160), Point(100, 140), Point(100, 120))

obj.draw(win)

win.getMouse()
win.close()