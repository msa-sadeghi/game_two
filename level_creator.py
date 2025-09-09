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
        pygame.draw.line(screen, "red", (i * TILE_SIZE -scroll , 0), (i * TILE_SIZE -scroll, HEIGHT))

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
                screen.blit(all_button[world_data[i][j]].image, (j * TILE_SIZE - scroll, i * TILE_SIZE))

scroll = 0
scroll_left = False
scroll_right = False
current_level = 1

font = pygame.font.SysFont("arial", 22)

current_level_text = font.render(f"level:{current_level}",  True, "red")

FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
                
    if scroll_left and scroll > 0:
        scroll -= 5
    if scroll_right:
        scroll += 5    
    screen.fill("black")
    draw_grid()
    draw_tiles()
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, RIGHT_MARGIN, HEIGHT + BOTTOM_MARING))
    pygame.draw.rect(screen, "lightgreen", (0, HEIGHT, WIDTH + RIGHT_MARGIN, BOTTOM_MARING))
    for i,btn in enumerate(all_button):
        btn.draw(screen)
        if btn.handle_click():
            selected_btn_index = i

    pygame.draw.rect(screen,"red", all_button[selected_btn_index].rect, 3)
    
    mouse_position = pygame.mouse.get_pos()
    r = mouse_position[1] // TILE_SIZE
    c = (mouse_position[0] + scroll) // TILE_SIZE
    if pygame.mouse.get_pressed()[0] and mouse_position[0] < WIDTH and mouse_position[1] < HEIGHT:
        world_data[r][c] =  selected_btn_index
    if pygame.mouse.get_pressed()[2] and mouse_position[0] < WIDTH and mouse_position[1] < HEIGHT:
        world_data[r][c] = -1
    

    screen.blit(current_level_text, (10, HEIGHT + 20))

    pygame.display.update()
    CLOCK.tick(FPS)

