from bomb import Bomb
from box import Box
from energy import Energy
from obstacle import Obstacle
import pygame
import os
TILE_SIZE = 50
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


all_images = objects_images + tiles_images

class World:
    def __init__(self, world_data, bomb_group, box_group, energy_group, obstacle_group):
        self.boxes = []
        self.bombs = []
        self.energy = []
        self.doors = []

        for i in range(len(world_data)):
            for j in range(len(world_data[i])):
                if world_data[i][j] == 0:
                    b = Bomb(all_images[0], j * TILE_SIZE, i *  TILE_SIZE, bomb_group)
                    self.bombs.append(b)
                elif world_data[i][j] == 1:
                    b = Energy(all_images[1], j * TILE_SIZE, i *  TILE_SIZE, energy_group)
                    self.energy.append(b)

                elif world_data[i][j] in (13, 14, 15, 16):

                    b = Box(all_images[world_data[i][j]], j * TILE_SIZE, i *  TILE_SIZE, box_group)
                    self.boxes.append(b)
                elif world_data[i][j] == 21:

                    b = Obstacle(all_images[world_data[i][j]], j * TILE_SIZE, i *  TILE_SIZE, obstacle_group)
                    # self.boxes.append(b)
