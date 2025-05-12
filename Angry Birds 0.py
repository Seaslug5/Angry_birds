import pymunk, pygame
from intro import space, body

# Oh! gravity works...
space.gravity = (0, 50)

#Floor
floor = pymunk.Segment(space.static_body, (0, 400), (800, 400), 5)
floor.elasticity = 0.5
floor.friction = 1.0
space.add(floor)

box = pymunk.Poly.create_box(body, (50,50))   
#shape = pymunk.Poly(body, ((-50, 0), (0, 0), (0,-50), (-50,-50 )))
def create_box(x, y, size=(50, 50)):
    mass = 1
    moment = pymunk.moment_for_box(mass, size)
    body = pymunk.Body(mass, moment)
    body.position = (x, y)
    shape = pymunk.Poly.create_box(body, size)
    shape.elasticity = 0.5
    shape.friction = 2.0
    space.add(body, shape)

# Create multiple boxes at different positions
create_box(100, 80)
create_box(100, 120)
create_box(100, 160)


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
        #print(f"Mouse pressed at: ({x}, {y})")
        create_box(x, y)

space.add(body)
App().run()