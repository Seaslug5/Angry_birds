import pymunk
from intro import App, body, space
pts = [(10, 10), (690, 10), (690, 230), (10, 230), (10, 0)]
for i in range(len(pts)-1):
    seg = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%len(pts)], 2)
    seg.elasticity = .999
    space.add(seg)
#Segments
def shape(X, Y):

    body = pymunk.Body(mass=1, moment=1000)
    body.position = (X, Y)
    body.apply_impulse_at_local_point
    shape = pymunk.Segment(body, (-50, 0), (0, 0), radius=10)
    shape2 = pymunk.Segment(body, (0, 0), (0, 50), radius = 10)
    shape.elasticity = 0.999
    space.add(body, shape, shape2)
shape (101, 101)

#help make circle! please
#Circle

   
#Trianges
def shape(X, Y):
    body = pymunk.Body(mass=1, moment=1000)
    body.position = (X, Y)
    body.apply_impulse_at_local_point((100, 0), (0, 1))
    shape = pymunk.Poly(body, ((-50, 0), (0, 0), (0,-50)))
    shape.elasticity = 0.99
    space.add(body, shape)
shape(100, 100)
shape(50, 100)
shape(200, 50)
App().run()