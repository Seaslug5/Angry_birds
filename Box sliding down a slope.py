import pymunk
import pygame
from intro import body, space, App

box = pymunk.Poly.create_box(body, (50, 50))
box.elasticity = 0.6
space.add(box)
App().run()