import pygame
pygame.init()
import os
from button import Button

WIDTH = 1000
HEIGHT = 600
RIGHT_MARGIN = 400
BOTTOM_MARING = 100
TILE_SIZE = 50
screen = pygame.display.set_mode((WIDTH + RIGHT_MARGIN, HEIGHT + BOTTOM_MARING))
CLOCK = pygame.time.Clock()

objects_images = []
for image_name in os.listdir("./freescifiplatform/png/Objects"):
    img = pygame.image.load(f"./freescifiplatform/png/Objects/{image_name}")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    objects_images.append(img)

tiles_images = []
for image_name in os.listdir("./freescifiplatform/png/Tiles"):
    img = pygame.image.load(f"./freescifiplatform/png/Tiles/{image_name}")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    tiles_images.append(img)


objects_buttons = []
r = 0
c = 0
for img in objects_images:
    btn = Button(img,  WIDTH + 50 + c * (TILE_SIZE +  20), 50 + r * (TILE_SIZE + 20))
    objects_buttons.append(btn)
    c += 1
    if c == 5:
        c = 0
        r += 1

tiles_buttons = []
for img in tiles_images:
    btn = Button(img,  WIDTH + 50 + c * (TILE_SIZE +  20), 50 + r * (TILE_SIZE + 20))
    tiles_buttons.append(btn)
    c += 1
    if c == 5:
        c = 0
        r += 1

all_button = objects_buttons + tiles_buttons


COLS = 150
ROWS = HEIGHT // TILE_SIZE

def draw_grid():
    for i in range(ROWS + 1):
        pygame.draw.line(screen, "red", (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE))
    for i in range(COLS + 1):
        pygame.draw.line(screen, "red", (i * TILE_SIZE , 0), (i * TILE_SIZE, HEIGHT))

selected_btn_index = 0
r = 0
c = 0

world_data = []
for i in range(ROWS):
    row = [-1] * COLS
    world_data.append(row)

def draw_tiles():
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] != -1:
                screen.blit(all_button[world_data[i][j]].image, (j * TILE_SIZE, i * TILE_SIZE))




FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    draw_grid()
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, RIGHT_MARGIN, HEIGHT + BOTTOM_MARING))
    pygame.draw.rect(screen, "lightgreen", (0, HEIGHT, WIDTH + RIGHT_MARGIN, BOTTOM_MARING))
    for i,btn in enumerate(all_button):
        btn.draw(screen)
        if btn.handle_click():
            selected_btn_index = i

    pygame.draw.rect(screen,"red", all_button[selected_btn_index].rect, 3)
    draw_tiles()
    mouse_position = pygame.mouse.get_pos()
    r = mouse_position[1] // TILE_SIZE
    c = mouse_position[0] // TILE_SIZE
    if pygame.mouse.get_pressed()[0] and mouse_position[0] < WIDTH and mouse_position[1] < HEIGHT:
        world_data[r][c] =  selected_btn_index
    pygame.display.update()
    CLOCK.tick(FPS)

