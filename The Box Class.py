import pymunk
from intro import body, space, App


pts = [(150, 10), (690, 10), (690, 230), (10, 230), (10, 50)]
for i in range(len(pts)-1):
    seg = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%len(pts)], 2)
    seg.elasticity = .999
    space.add(seg)

class Box:
    def __init__(self, p0=(10, 10), p1=(690, 230), d=2):
        x0, y0 = p0
        x1, y1 = p1
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for i in range(4):
            segment = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%4], d)
            segment.elasticity = .8
            segment.friction = 1
            space.add(segment)


def shape(X, Y):

    body = pymunk.Body(mass=1, moment=1000)
    body.position = (X, Y)
    body.apply_impulse_at_local_point((100, 0), (0, 1))
    shape = pymunk.Segment(body, (-50, 0), (0, 0), radius=10)
    shape2 = pymunk.Segment(body, (0, 0), (0, 50), radius = 10)
    shape.elasticity = 0.999
    space.add(body, shape, shape2)
shape(100, 100)
shape(50, 100)
shape(200, 50)
App().run()