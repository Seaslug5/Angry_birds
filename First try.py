import pygame
import pymunk
import pymunk.pygame_util
pygame.init()
screen=pygame.display.set_mode((400, 500))
runing = True
while runing:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (0, 0, 255),(0, 0, 50, 50))
        pygame.display.flip()
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pygame.draw.rect(screen, (0, 0, 255),(50, 50, 50, 50))
                pygame.display.flip()

                print ("Move the charecter forwards")
            elif event.key == pygame.K_s:
                print ("Move the charecter backwards")
            elif event.key == pygame.K_a:
                print ("Move the charecter left")
            elif event.key == pygame.K_d:
                print ("Move the charecter right")
            pygame.display.flip()

        if event.type ==pygame.quit:
            running = False

