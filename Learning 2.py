import random
import pymunk, pygame
import pymunk.pygame_util
space = pymunk.Space()
body = pymunk.Body (mass=1, moment=10)

pygame.init()

# Screen setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Pymunk setup
space = pymunk.Space()
space.gravity = (0, 900)

# Player setup (a dynamic box)
player_body = pymunk.Body(1, pymunk.moment_for_box(1, (50, 50)))
player_body.position = (400, 300)
player_shape = pymunk.Poly.create_box(player_body, (50, 50))
player_shape.friction = 1.0
space.add(player_body, player_shape)

def update(self, events, dt):
    pressed = pygame.key.get_pressed()
    move = pygame.Vector2((0, 0))
    if pressed[pygame.K_w]: move += (0, -1)
    if pressed[pygame.K_a]: move += (-1, 0)
    if pressed[pygame.K_s]: move += (0, 1)
    if pressed[pygame.K_d]: move += (1, 0)
    if move.length() > 0: move.normalize_ip()
    self.pos += move*(dt/5)
    self.rect.center = self.pos

# Ground setup (static)
ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
ground_body.position = (0, screen_height - 50)
ground_shape = pymunk.Segment(ground_body, (0, 0), (2000, 0), 5)
ground_shape.friction = 1.0
space.add(ground_body, ground_shape)

# Camera vector
camera = pygame.Vector2(0, 0)

# Player control parameters
move_speed = 400

running = True
while running:
    dt = clock.tick(60) / 1000  # seconds elapsed this frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Simple left/right movement by applying forces
    if keys[pygame.K_LEFT]:
        player_body.apply_force_at_local_point((-move_speed, 0), (0, 0))
    elif keys[pygame.K_RIGHT]:
        player_body.apply_force_at_local_point((move_speed, 0), (0, 0))

    # Jump if on ground (simple check)
    if keys[pygame.K_SPACE]:
        # Check if player roughly on ground before jumping
        # (You might want a more robust ground check)
        if abs(player_body.velocity.y) < 0.1:
            player_body.apply_impulse_at_local_point((0, -15000))

    # Step physics
    space.step(dt)

    # Update camera to follow player center x, smooth lerp
    target_x = player_body.position.x - (screen_width / 2)
    lerp_factor = 0.1
    camera.x += (target_x - camera.x) * lerp_factor
    # Optional: keep camera y fixed (ground-level view)
    camera.y = 0

    # Clear screen
    screen.fill((30, 30, 30))

    # Draw ground (adjusted by camera)
    ground_start = (ground_shape.a[0] - camera.x, ground_shape.a[1] - camera.y)
    ground_end = (ground_shape.b[0] - camera.x, ground_shape.b[1] - camera.y)
    pygame.draw.line(screen, (200, 200, 200), ground_start, ground_end, 5)

    # Draw player (adjusted by camera)
    player_rect = pygame.Rect(0, 0, 50, 50)
    player_rect.center = (player_body.position.x - camera.x, player_body.position.y - camera.y)
    pygame.draw.rect(screen, (100, 200, 100), player_rect)

    pygame.display.flip()

pygame.quit()


# # Oh! gravity works...
# space.gravity = (0, 900)


# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((32, 32))
#         self.image.fill(pygame.Color('dodgerblue'))
#         self.rect = self.image.get_rect()
#         self.pos = pygame.Vector2((100, 200))



# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((500, 500))
#     clock = pygame.time.Clock()
#     dt = 0
#     player = Player()
#     sprites = pygame.sprite.Group(player)
#     # the "world" is now bigger than the screen
#     # so we actually have anything to move the camera to
#     background = pygame.Surface((1500, 1500))
#     background.fill((30, 30, 30))

#     # a camera is just two values: x and y
#     # we use a vector here because it's easier to handle than a tuple
#     camera = pygame.Vector2((0, 0))

#     for _ in range(3000):
#         x, y = random.randint(0, 1000), random.randint(0, 1000)
#         pygame.draw.rect(background, pygame.Color('green'), (x, y, 2, 2))

#     while True:
#         events = pygame.event.get()
#         for e in events:
#             if e.type == pygame.QUIT:
#                 return

       
#         # move the camera around
#         pressed = pygame.key.get_pressed()
#         camera_move = pygame.Vector2()
#         if pressed[pygame.K_UP]: camera_move += (0, 1)
#         if pressed[pygame.K_LEFT]: camera_move += (1, 0)
#         if pressed[pygame.K_DOWN]: camera_move += (0, -1)
#         if pressed[pygame.K_RIGHT]: camera_move += (-1, 0)
#         if camera_move.length() > 0: camera_move.normalize_ip()
        
#         camera += camera_move*(dt/5)



# if __name__ == '__main__':
#     main()

# space.add(body)
# #App().run()