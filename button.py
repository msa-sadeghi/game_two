import pygame
class Button:
    def __init__(self, image, x,y):
        self.image = image
        self.rect = self.image.get_rect(
            center = (x,y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_click(self):
        clicked = False
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0]:
                clicked = True
        return clicked