import pymunk, pygame
import pymunk.pygame_util

space = pymunk.Space()
body = pymunk.Body (mass=1, moment=10)
# Oh! gravity works...
space.gravity = (0, 50)

#Floor
floor = pymunk.Segment(space.static_body, (0, 400), (800, 400), 5)
floor.elasticity = 0.5
floor.friction = 1.0
space.add(floor)

#Create the boxes
box = pymunk.Poly.create_box(body, (50,50))   
def create_box(x, y, size=(50, 50)):
    mass = 1
    moment = pymunk.moment_for_box(mass, size)
    boxBody = pymunk.Body(mass, moment)
    boxBody.position = (x, y)
    shape = pymunk.Poly.create_box(boxBody, size)
    shape.elasticity = 0.5
    shape.friction = 2.0
    space.add(boxBody, shape)

#Create the circles
def create_circle(x, y, radius=20):
    mass = 1
    moment = pymunk.moment_for_circle(mass, radius, radius)
    circleBody = pymunk.Body(mass, moment)
    circleBody.position = (x, y)
    shape = pymunk.Circle(circleBody, radius)
    shape.elasticity = 0.5
    shape.friction = 2.0
    space.add(circleBody, shape)

#creating the tower
create_box(600, 350)
create_box(650, 350)
create_box(700, 350)
#2nd layer
create_box(625, 300)
create_box(675, 300)
#stack
create_box(650, 250)
create_box(650, 200)
create_box(650, 150)
#Top
create_box(625, 100)
create_box(675, 100)
create_box(650, 50)


#discribing self and telling it when to run
class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Mouse press handler
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.on_mouse_press(x, y)

            # Update physics and render here (the number is an RGB for grey)
            self.screen.fill((220, 220, 220))
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.01)
            pygame.display.flip()
            self.clock.tick(60)
#draws box on click
    def on_mouse_press(self, x, y):
        create_circle(x, y)

space.add(body)
App().run()