from pygame.sprite import Sprite
import pygame
import os
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.animation_names = os.listdir("./ninjagirlnew")
        self.all_images = []
        for animation in self.animation_names:
            temp_list = []
            images_names = os.listdir(f"./ninjagirlnew/{animation}")
            for im_name in images_names:
                img = pygame.image.load(f"./ninjagirlnew/{animation}/{im_name}")
                img = pygame.transform.scale_by(img, 0.4)
                temp_list.append(img)
            self.all_images.append(temp_list)
        self.animation_index = 4
        self.frame_index = 0
        self.image = self.all_images[self.animation_index][self.frame_index]
        self.rect =  self.image.get_rect(topleft=(x,y))
        self.last_animation_time = pygame.time.get_ticks()
        self.direction = 1
        self.idle = True
        self.yspeed = 0
    def draw(self, screen):
        img = pygame.transform.flip(self.image, self.direction == -1, False)
        screen.blit(img, self.rect)
    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.idle = False
            self.direction = -1
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.idle = False
            self.direction = 1
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True
        if keys[pygame.K_UP]:
            self.yspeed = -15
        
        dy += self.yspeed
        self.yspeed += 1
        self.rect.x += dx
        self.rect.y += dy

    def handle_animation(self):
        self.image = self.all_images[self.animation_index][self.frame_index]
        if pygame.time.get_ticks() - self.last_animation_time > 100:
            self.last_animation_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.animation_index]):
                self.frame_index = 0

    def change_animation(self, animation_index):
        if animation_index != self.animation_index:
            self.animation_index = animation_index
            self.frame_index = 0





