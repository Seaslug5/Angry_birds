import pymunk
from intro import App, body, space
pts = [(10, 10), (690, 10), (690, 230), (10, 230), (10, 0)]
for i in range(len(pts)-1):
    seg = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%len(pts)], 2)
    seg.elasticity = .999
    space.add(seg)

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
  