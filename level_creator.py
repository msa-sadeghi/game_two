import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600
RIGHT_MARGIN = 400
BOTTOM_MARING = 100
screen = pygame.display.set_mode((WIDTH + RIGHT_MARGIN, HEIGHT + BOTTOM_MARING))
CLOCK = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, RIGHT_MARGIN, HEIGHT + BOTTOM_MARING))
    pygame.draw.rect(screen, "lightgreen", (0, HEIGHT, WIDTH + RIGHT_MARGIN, BOTTOM_MARING))
    pygame.display.update()
    CLOCK.tick(FPS)

