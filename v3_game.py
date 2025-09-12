import numpy
import pygame
import math
import sys

#setting up the environment

pygame.init()
width, height = 1200, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projectile Simulator")
clock = pygame.time.Clock()

button_fire = pygame.Rect(1050, 600, 100, 50)
fired = False
x, y = 0, 0
vx, vy = 0, 0
time = 0
speed = 20
g = 9.81
angle = 45
scale = 50

#main game loop

while True:
    dt = clock.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_fire.collidepoint(event.pos) and not fired:
                fired = True
                theta = math.radians(angle)
                vx = speed * math.cos(theta)
                vy = speed * math.sin(theta)

                #resetting projectile
                x, y = 0, 0
                time = 0
            

    #Physics section

    if fired:
        time += dt
        x = vx * time
        y = vy * time - ((0.5*g)*(time**2))

        if y < 0 and time > 0:
            y = 0  # ball on da ground
            fired = False

    #Drawing/animation section
    pygame.draw.rect(screen, (135, 206, 235), (0, 0, width, int(0.65*height)))
    pygame.draw.rect(screen, (34, 139, 34), (0, int(0.65 * height), width, int(0.35*height)))
    pygame.draw.rect(screen, (255, 0, 0), button_fire) #red button
    font = pygame.font.SysFont(None, 36)
    text = font.render("FIRE", True, (255, 165, 0))
    screen.blit(text, (button_fire.x + 20, button_fire.y + 10))

    if fired or y == 0:
        start_x = (130)
        start_y = 75
        
        px = start_x + int(x*scale)
        py = start_y + int(height * 0.6 - (y*scale))
        pygame.draw.circle(screen, (200, 50, 50), (px, py), 8)

    pygame.display.flip()

    