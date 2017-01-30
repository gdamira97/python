'''import turtle

def printEscape(event):
    print('Escape')
    
def printSymbol(event):
    print(event.char)

def showCoordinates(event):
    print(event.x, ', ', event.y)
    turtle.penup()
    
def drawByCoordinates(event):
    print(event.x, ', ', event.y)
    turtle.goto(event.x-290, 270-event.y)
    turtle.pendown()
    
def penUp(event):
    turtle.penup()
    
turtle.speed(0)
c=turtle.getcanvas()
c.bind('<Escape>', printEscape)
c.bind('<Key>', printSymbol)
c.bind('<Button-1>', showCoordinates)
c.bind('<ButtonRelease-1>', penUp)
c.bind('<B1-Motion>', drawByCoordinates)
s=turtle.Screen()
turtle.listen()
turtle.done()
'''
'''
import turtle

def gothere(event):
     print (event.x)
     print (event.y)
     turtle.goto(event.x,event.y)

turtle.reset()
turtle.speed(0)

c=turtle.getcanvas()

c.bind("<Button-1>", gothere)

turtle.pendown()
'''
import turtle

def gothere(event):
     turtle.penup()
     turtle.goto(event.x-360,340-event.y)
     turtle.pendown()

def movearound(event):
     turtle.goto(event.x-360,340-event.y)

def release(event):
     turtle.penup()

def reset(event):
     turtle.clear()

turtle.reset()
turtle.speed(0)

c=turtle.getcanvas()

c.bind("<Button-1>", gothere)
c.bind("<B1-Motion>", movearound)
c.bind("<ButtonRelease-1>", release)
c.bind("<Escape>",reset)

s=turtle.Screen()
s.listen()
'''
import turtle
class MyTurtle(object):
    self=turtle.Turtle()
    def glow(self,x,y):
         self=turtle.fillcolor("red")
    def unglow(self,x,y):
         self=turtle.fillcolor("")

t = MyTurtle()
turtle.onclick(t.glow)
turtle.onrelease(t.unglow) 
'''
