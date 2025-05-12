import pygame
import pymunk
import pymunk.pygame_util

space = pymunk.Space()
b0= space.static_body
space.gravity = 0, 10

body = pymunk.Body (mass=1, moment=10)
body.position = 100, 50
circle = pymunk.Circle(body, radius=20)
circle.elasticity = 0.5
circle.friction = 0.5
#space.add(body, circle)

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 240))
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True
    def run(self):
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.image.save(self.screen, 'intro.png')
                self.screen.fill((220, 220, 220))
                space.debug_draw(self.draw_options)
                pygame.display.update()
                space.step(0.01)
            pygame.quit()