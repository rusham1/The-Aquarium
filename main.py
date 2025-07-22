import pygame
from fish import Fish,generate_random_fish
from environment import generate_rocks, draw_rocks,generate_plants, draw_plants


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Aquarium")

clock = pygame.time.Clock()

# Rocks and Fish
rocks = generate_rocks()

plants = generate_plants()



# Generate a list of random fish
fishes = [generate_random_fish(WIDTH, HEIGHT) for _ in range(10)]  # You can adjust the number


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 100, 200))  # Aqua blue

    draw_plants(screen, plants)  # Draw plants first (background)
    draw_rocks(screen, rocks)    # Then rocks (foreground)

    for fish in fishes:
        fish.move(WIDTH)
        fish.draw(screen)

    draw_rocks(screen, rocks)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
