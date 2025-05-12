import pygame, pymunk
from intro import space, body, App
from random import randint

space.gravity = 0, 10
for i in range(40):
    body = pymunk.Body(mass=1, moment=10)
    body.position = randint(40, 660), randint(40, 200)
    impulse = randint(-100, 100), randint(-100, 100)
    body.apply_impulse_at_local_point(impulse)
    circle = pymunk.Circle(body, radius=10)
    circle.elasticity = 0.8
    circle.friction = 0.5
    space.add(body, circle)
App().run