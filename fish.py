import pygame
import random


class Fish:
    def __init__(self,x,y,speed,size_x,size_y,color):
        self.x=x
        self.y=y
        self.speed=speed
        self.size_x=size_x
        self.size_y=size_y
        self.color=color

    def move(self,width):
        self.x+=self.speed
        if self.x>width or self.x< 0:
            self.speed*= -1

    def draw(self,screen):
        fx, fy, fsx, fsy = self.x, self.y, self.size_x, self.size_y
        fs = self.speed
        fc = self.color

        pygame.draw.ellipse(screen, fc, (fx, fy, fsx, fsy))
        eye_x = fx + (fsx * 0.75 if fs > 0 else fsx * 0.25)
        eye_y = fy + fsy * 0.4
        pygame.draw.circle(screen, (0, 0, 0), (int(eye_x), int(eye_y)), 2)

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

def generate_random_fish(max_width, max_height):
    x = random.randint(0, max_width)
    y = random.randint(0, max_height - 100)
    speed = random.choice([-1, 1]) * random.uniform(0.5, 2.5)
    size_x = random.randint(30, 60)
    size_y = random.randint(15, 30)
    color = (
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255)
    )
    return Fish(x, y, speed, size_x, size_y, color)

