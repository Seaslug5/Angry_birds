import random
import pymunk, pygame
import pymunk.pygame_util
space = pymunk.Space()
body = pymunk.Body (mass=1, moment=10)
#trying again on a different tab *see Learning 2*

# Oh! gravity works...
space.gravity = (0, 900)

#Floor
def create_ground():
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, (0, 550), (800, 550), 5)
    shape.friction = 1.0
    space.add(body, shape)


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        camera = pygame.Vector2((0, 0))
        background = pygame.Surface((1500, 1500))
        background.fill((30, 30, 30))
        for _ in range(3000):
            x, y = random.randint(0, 1000), random.randint(0, 1000)
            pygame.draw.rect(background, pygame.Color('green'), (x, y, 2, 2))
        while self.running:
            events=pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_body.apply_impulse_at_local_point((-50, 0))
            if keys[pygame.K_RIGHT]:
                    player_body.apply_impulse_at_local_point((50, 0))
            if keys[pygame.K_SPACE] and abs(player_body.velocity.y) < 1:  # Jump
                player_body.apply_impulse_at_local_point((0, -100))
                # Mouse press handler
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                self.on_mouse_press(x, y)
            #print ("It works!")
            create_ground()
            player_body = create_player()
        # copy/paste because I'm lazy
        # just move the camera around
            pressed = pygame.key.get_pressed()
            camera_move = pygame.Vector2()
            if pressed[pygame.K_UP]: camera_move += (0, 1)
            if pressed[pygame.K_LEFT]: camera_move += (1, 0)
            if pressed[pygame.K_DOWN]: camera_move += (0, -1)
            if pressed[pygame.K_RIGHT]: camera_move += (-1, 0)
            if camera_move.length() > 0: camera_move.normalize_ip()
            camera += camera_move#*(dt/5)

        #body = sprites
            sprites = pygame.sprite.Group(player_body)
            sprites.update(events)#, dt)
        
            # before drawing, we shift everything by the camera's x and y values
            self.screen.blit(background, camera)
            for s in sprites:
                self.screen.blit(s.image, s.rect.move(*camera))

                # Update physics and render here (the number is an RGB for grey)
                self.screen.fill((220, 220, 220))
                space.debug_draw(self.draw_options)
                pygame.display.update()
                space.step(0.01)
                pygame.display.flip()
                self.clock.tick(60)

# Create a player (a simple circle for now)
def create_player():
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 25))
    body.position = (100, 500)
    shape = pymunk.Circle(body, 25)
    shape.elasticity = 0.5
    shape.friction = 1.0
    space.add(body, shape)
    return body


 # a camera is just two values: x and y
    # we use a vector here because it's easier to handle than a tuple



# while True:
    #events = pygame.event.get()
           
# Initialize objects
    


 

space.add(body)
App().run()