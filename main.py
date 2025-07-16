import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Aquarium")

clock = pygame.time.Clock()

import random

# Generate a list of rocks with random sizes, colors, and positions
rocks = []
for _ in range(250):  # Number of rocks
    rock_width = random.randint(15, 40)
    rock_height = random.randint(10, 25)
    x_pos = random.randint(0, WIDTH - rock_width)
    y_pos = HEIGHT - rock_height   # Just above the bottom edge
    color_value = random.randint(50, 150)
    rock_color = (color_value, color_value, color_value)  # Shades of gray
    rocks.append({'x': x_pos, 'y': y_pos, 'w': rock_width, 'h': rock_height, 'color': rock_color})

# Define fish
fishes = [
    {'x': 100, 'y': 500, 'speed': 1, 'fishSizeX': 40, 'fishSizeY': 20, 'fishColor': (255, 200, 0)},
    {'x': 300, 'y': 400, 'speed': -2, 'fishSizeX': 50, 'fishSizeY': 25, 'fishColor': (0, 255, 150)},
    {'x': 600, 'y': 200, 'speed': 1.5, 'fishSizeX': 35, 'fishSizeY': 18, 'fishColor': (100, 100, 255)},
    {'x': 200, 'y': 100, 'speed': -1.2, 'fishSizeX': 60, 'fishSizeY': 30, 'fishColor': (255, 100, 100)}
]

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 100, 200))  #Aqua blue background

    for fish in fishes:
        fsx, fsy, fc = fish['fishSizeX'], fish['fishSizeY'], fish['fishColor']
        fs, fx, fy = fish['speed'], fish['x'], fish['y']
        fx += fs
        if fx > WIDTH or fx < 0:
            fs *= -1
            fish['speed'] = fs
        fish['x'] = fx

        # Fish body
        pygame.draw.ellipse(screen, fc, (fx, fy, fsx, fsy))
        eye_x = fx + (fsx * 0.75 if fs > 0 else fsx * 0.25)
        eye_y = fy + fsy * 0.4
        pygame.draw.circle(screen, (0, 0, 0), (int(eye_x), int(eye_y)), 2)

        # Fins and Tail
        if fs > 0:
            fin2_points = [(fx+fsx*0.35, fy), (fx+fsx*0.4 - fs*2, fy-fsy*0.8), (fx+fsx*0.45, fy)]
            fin1_points = [(fx+fsx*0.35, fy+fsy/2), (fx+fsx*0.4 - fs*2, fy+fsy*1.8), (fx+fsx*0.45, fy+fsy/2)]
            tail_points = [(fx+0.1*fsx, fy+fsy/2), (fx-fsy/2, fy), (fx-fsy/2, fy+fsy)]
        else:
            fin2_points = [(fx+fsx*0.65, fy), (fx+fsx*0.6-fs*2, fy-fsy*0.8), (fx+fsx*0.55, fy)]
            fin1_points = [(fx+fsx*0.65, fy+fsy), (fx+fsx*0.6-fs*2, fy+fsy*1.8), (fx+fsx*0.55, fy+fsy)]
            tail_points = [(fx+fsx-0.1*fsx, fy+fsy/2), (fx+fsx+fsy/2, fy), (fx+fsx+fsy/2, fy+fsy)]

        pygame.draw.polygon(screen, fc, tail_points)
        pygame.draw.polygon(screen, fc, fin1_points)
        pygame.draw.polygon(screen, fc, fin2_points)

    for rock in rocks:
        pygame.draw.ellipse(screen, rock['color'], (rock['x'], rock['y'], rock['w'], rock['h']))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
