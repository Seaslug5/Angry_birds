import pymunk
from intro import space, App
b0 = space.static_body
for i in range(1, 6):
    circlex=40*i
    circley=100
    if i==1:
        circlex =-10
        circley=50
    body = pymunk.Body(mass=1, moment=10)
    body.position = (circlex, circley)
    circle = pymunk.Circle(body, radius=20)
    circle.elasticity=1.009
    joint = pymunk.PinJoint(b0, body, (40*i, 50))
    space.add (body, circle, joint)
    
App().run()