import pymunk, pygame
from intro import space, App

pts = [(10, 10), (690, 10), (690, 230), (10, 230)]
for i in range(4):
    seg = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%4], 2)
    seg.elasticity = 0.999
    space.add(seg)
    body = pymunk.Body(mass=1, moment=10)
    body.position = (100, 200)
    body.apply_impulse_at_local_point((100, 0))
App().run()
