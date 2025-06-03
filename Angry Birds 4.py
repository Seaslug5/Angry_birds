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
    shape.color = pygame.Color("darkGreen")
    space.add(boxBody, shape)
    return shape

#Box=Pig Pig takes three hit points and then "dies"


def create_Hplane(x, y, size=(200, 25)):
    mass = 3
    moment = pymunk.moment_for_box(mass, size)
    HplaneBody = pymunk.Body(mass, moment)
    HplaneBody.position = (x, y)  
    shape = pymunk.Poly.create_box(HplaneBody, size)
    shape.elasticity = 0.5
    shape.friction = 2.0
    space.add(HplaneBody, shape)
    return HplaneBody, shape


def create_Vplane(x, y, size=(25, 200)):
    mass = 3
    moment = pymunk.moment_for_box(mass, size)
    VplaneBody = pymunk.Body(mass, moment)
    VplaneBody.position = (x, y)  
    shape = pymunk.Poly.create_box(VplaneBody, size)
    shape.elasticity = 0.5
    shape.friction = 2.0
    space.add(VplaneBody, shape)
    return VplaneBody, shape



#Create the circles
def create_circle(x, y, radius=20):
    mass = 1
    
    moment = pymunk.moment_for_circle(mass, 0, radius)
    circleBody = pymunk.Body(mass, moment)
    circleBody.position = (x, y)
    circleBody.velocity = [300,0]
    shape = pymunk.Circle(circleBody, radius)
    shape.elasticity = 0.9
    shape.friction = 2.0
    space.add(circleBody, shape)
    shape.color = pygame.Color("red")
    return shape



#test

# Define a callback function for when objects begin touching
def on_collision_begin(arbiter, space, data):
    print("Objects have touched!")
    return True  # Return True to process the collision normally
# Simulate the space
#for _ in range(100):
    #space.step(0.02)



#Structure
create_Vplane(700, 300)
create_Vplane(550, 300)
create_Hplane(625, 175)
pig0 = create_box(625, 350)
pig0.colision_type = 1
pig1 = create_box(625, 150)
pig1.colision_type = 1


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
#draws Bird on click
    def on_mouse_press(self, x, y):
        bird = create_circle(x, y)
        bird.colision_type = 2

        # Add a collision handler for the two collision types
        handler = space.add_collision_handler(1, 2)
        handler.begin = on_collision_begin
space.add(body)
App().run()