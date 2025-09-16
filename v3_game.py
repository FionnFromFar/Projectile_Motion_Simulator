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
font = pygame.font.SysFont(None, 36)
font_big = pygame.font.SysFont(None, 50)
button_fire = pygame.Rect(1050, 600, 115, 50)
button_reload = pygame.Rect(1050, 520, 115, 50)
button_start = pygame.Rect(width//2 - 100, height//2 - 40, 200, 80)
fired = False
speed = 10
g = 9.81
angle = 45
scale = 50
projectile_stats = []
game_started = False

#setting up the speed slider:
slider_track_x = 200
slider_track_y = 600
slider_width = 300
slider_height = 5
knob_radius = 10
speed_min = 1
speed_max = 15
slider_x = int(slider_track_x + (speed - speed_min) / (speed_max - speed_min) * slider_width)
dragging_speed = False

#setting up the angle slider:
slider_angle_x = 200
slider_angle_y = 650
slider_angle_width = 300
slider_angle_height = 5
angle_min = 0
angle_max = 90
slider_angle_xpos = int(slider_angle_x + (angle - angle_min) / (angle_max - angle_min) * slider_angle_width)
dragging_angle = False


#main game loop

while True:
    dt = clock.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_start.collidepoint(event.pos) and not game_started:
                game_started = True
                new_proj = {
                    "x": 0,
                    "y": 0,
                    "vx": speed * math.cos(math.radians(angle)),
                    "vy": speed * math.sin(math.radians(angle)),
                    "time": 0,
                    "active": False,
                    "color": (200, 50, 50)
                }
                projectile_stats.append(new_proj)

            elif button_reload.collidepoint(event.pos):
                new_proj = {
                    "x": 0,
                    "y": 0,
                    "vx": speed * math.cos(math.radians(angle)),
                    "vy": speed * math.sin(math.radians(angle)),
                    "time": 0,
                    "active": False,
                    "color": (200, 50, 50)
                }
                projectile_stats.append(new_proj)

            elif button_fire.collidepoint(event.pos):
                if projectile_stats:
                    last = projectile_stats[-1]
                    if (not last["active"]) and (last["y"] == 0):
                        last["vx"] = speed * math.cos(math.radians(angle))
                        last["vy"] = speed * math.sin(math.radians(angle))
                        last["active"] = True
                        last["time"] = 0
                        fired = True
        
        
            mx, my = event.pos
            if (mx - slider_x)**2 + (my - slider_track_y)**2 <= knob_radius**2: #speed slider
                dragging_speed = True
            elif (mx - slider_angle_xpos)**2 + (my - slider_angle_y)**2 <= knob_radius**2: #angle slider
                dragging_angle = True
    

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_speed = False
            dragging_angle = False
            
        elif event.type == pygame.MOUSEMOTION:
            mx, my = event.pos
            #speed slider
            if dragging_speed:
                slider_x = max(slider_track_x, min(slider_track_x + slider_width, mx))
                slider_percent = (slider_x - slider_track_x) / slider_width
                speed = speed_min + slider_percent * (speed_max - speed_min)
            #angle slider
            if dragging_angle:
                slider_angle_xpos = max(slider_angle_x, min(slider_angle_x + slider_angle_width, mx))
                slider_angle_percent = (slider_angle_xpos - slider_angle_x) / slider_angle_width
                angle = angle_min + slider_angle_percent * (angle_max - angle_min)


    #Physics section

    for proj in projectile_stats:
        if proj["active"]:
            proj["time"] += dt
            proj["x"] = proj["vx"] * proj["time"]
            proj["y"] = proj["vy"] * proj["time"] - 0.5 * g * (proj["time"]**2)

            if proj["y"] < 0:
                proj["y"] = 0
                proj["active"] = False
                fired = False



    #Drawing/animation section

    #starting screen
    if not game_started:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (135, 206, 235), (0, 0, width, int(0.65*height))) #sky
        pygame.draw.rect(screen, (34, 139, 34), (0, int(0.65 * height), width, int(0.35*height))) #grass
        pygame.draw.rect(screen, (0, 255, 0), button_start)
        text_start = font_big.render("START", True, (0, 128, 0))
        screen.blit(text_start, (button_start.x + 45, button_start.y + 25))
        pygame.display.flip()

    #main game screen
    elif game_started:
        pygame.draw.rect(screen, (135, 206, 235), (0, 0, width, int(0.65*height))) #sky
        pygame.draw.rect(screen, (34, 139, 34), (0, int(0.65 * height), width, int(0.35*height))) #grass
        pygame.draw.rect(screen, (255, 0, 0), button_fire) #red button
        pygame.draw.rect(screen, (0, 100, 0), button_reload) #green reload button same size as 
        pygame.draw.rect(screen, (200, 200, 200), (slider_track_x, slider_track_y - slider_height//2, slider_width, slider_height)) #speed slider track
        pygame.draw.rect(screen, (200, 200, 200), (slider_angle_x, slider_angle_y - slider_angle_height//2, slider_angle_width, slider_angle_height)) #angle slider track
        pygame.draw.circle(screen, (255, 0, 0), (slider_x, slider_track_y), knob_radius) #speed slider knob
        pygame.draw.circle(screen, (255, 0, 0), (slider_angle_xpos, slider_angle_y), knob_radius)
        text_fire = font.render("FIRE", True, (255, 165, 0))
        text_reload = font.render("RELOAD", True, (0, 128, 128))
        text_speed = font.render(f"Speed: {int(speed)}", True, (0, 0, 0))
        text_angle = font.render(f"Angle: {int(angle)}", True, (0, 0, 0))
        screen.blit(text_fire, (button_fire.x + 30, button_fire.y + 10))
        screen.blit(text_reload, (button_reload.x + 7, button_reload.y + 10))
        screen.blit(text_speed, (slider_track_x, slider_track_y - 40))
        screen.blit(text_angle, (slider_angle_x, slider_angle_y - 40))
        

        for proj in projectile_stats:
            start_x = 130
            start_y = int(0.65 * height) + 40
            
            px = int(start_x + (proj["x"]* scale))
            py = int(start_y - (proj["y"] * scale))
            pygame.draw.circle(screen, proj["color"], (px, py), 8)

        pygame.display.flip()

    