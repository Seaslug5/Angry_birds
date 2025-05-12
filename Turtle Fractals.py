import turtle

turtle.speed('fastest')
turtle.right(-90)
angle = 30
def yaxis(size, lvl):   
  
    if lvl > 0:
        turtle.colormode(255)
        turtle.pencolor(0, 255//lvl, 0)
          
        turtle.forward(size)
        turtle.right(angle)
        yaxis(0.8 * size, lvl-1)
        turtle.pencolor(0, 255//lvl, 0)
        turtle.lt( 2 * angle )
        yaxis(0.8 * size, lvl-1)
        turtle.pencolor(0, 255//lvl, 0)
        turtle.right(angle)
        turtle.forward(-size)
           
yaxis(80, 8)
turtle.done()
