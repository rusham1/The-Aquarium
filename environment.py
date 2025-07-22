import random
import pygame

WIDTH, HEIGHT = 800, 600

def generate_rocks(num=250):
    rocks = []
    for _ in range(num):
        rock_width = random.randint(15, 40)
        rock_height = random.randint(10, 25)
        x_pos = random.randint(0, WIDTH - rock_width)
        y_pos = HEIGHT - rock_height
        color_value = random.randint(50, 150)
        rock_color = (color_value, color_value, color_value)
        rocks.append({'x': x_pos, 'y': y_pos, 'w': rock_width, 'h': rock_height, 'color': rock_color})
    return rocks

def draw_rocks(screen, rocks):
    for rock in rocks:
        pygame.draw.ellipse(screen, rock['color'], (rock['x'], rock['y'], rock['w'], rock['h']))

def generate_plants(num=30, width=800, height=600):
    plants = []
    for _ in range(num):
        plant_x = random.randint(0, width)
        plant_height = random.randint(40, 100)
        plant_width = random.randint(3, 7)
        plant_y = height - plant_height
        green_shade = random.randint(50, 150)
        color = (0, green_shade, 0)
        plants.append({'x': plant_x, 'y': plant_y, 'w': plant_width, 'h': plant_height, 'color': color})
    return plants

def draw_plants(screen, plants):
    for plant in plants:
        rect = pygame.Rect(plant['x'], plant['y'], plant['w'], plant['h'])
        pygame.draw.rect(screen, plant['color'], rect, border_radius=3)
