import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600

bg_image = pygame.image.load("./freegui/png/BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
menu_image = pygame.image.load("./freegui/png/Windows/Window_18.png")
menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
menu_image_rect = menu_image.get_rect()

start_game = False
def show_menu():
    screen.fill("pink")
    screen.blit(menu_image, menu_image_rect)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if start_game == False:
        show_menu()
    else:
        screen.blit(bg_image, (0,0))
    pygame.display.update()
    CLOCK.tick(FPS)

