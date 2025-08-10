import pygame
from button import Button
from player import Player
pygame.init()
my_player = Player(100, 380)
WIDTH = 1000
HEIGHT = 600
bg_image = pygame.image.load("./freegui/png/BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
menu_image = pygame.image.load("./freegui/png/Windows/Window_18.png")
menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
menu_image_rect = menu_image.get_rect()
click_image = pygame.image.load("./freegui/png/Buttons/Button_03.png")
click_button = Button(click_image, WIDTH//2 , HEIGHT//2)
start_game = False
def show_menu():
    global start_game
    screen.fill("pink")
    screen.blit(menu_image, menu_image_rect)
    click_button.draw(screen)
    if click_button.handle_click():
        start_game = True
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
        if my_player.idle:
            my_player.change_animation(4)
        elif not my_player.idle:
            my_player.change_animation(8)
        my_player.draw(screen)
        my_player.move()
        my_player.handle_animation()

    pygame.display.update()
    CLOCK.tick(FPS)

