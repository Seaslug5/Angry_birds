import pymunk
from intro import App, body, space
pts = [ (0, 235), (750, 235)]
for i in range(len(pts)-1):
    seg = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%len(pts)], 2)
    seg.elasticity = .01
    space.add(seg)
    seg.friction = 1
   
#Squares
def shape(X, Y):
    body = pymunk.Body(mass=1, moment=1000)
    body.position = (X, Y)
    shape = pymunk.Poly(body, ((-50, 0), (0, 0), (0,-50), (-50,-50 )))
    shape.elasticity = 0.01
    space.add(body, shape)
    shape.friction = 1
shape(100, 80)
shape(100, 180)
shape(100, 130)
App().run()