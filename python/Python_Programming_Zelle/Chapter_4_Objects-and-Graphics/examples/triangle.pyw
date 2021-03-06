#triangle.pyw
from graphics import *

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    #Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    #use Polygon object to draw the triangle
    tri = Polygon(p1,p2,p3)
    tri.setFill("peachpuff")
    tri.setOutline("cyan")
    tri.draw(win)

    message.setText("Click anywhere to quit.")
    win.getMouse()

main()