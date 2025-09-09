import pygame
class Button:
    def __init__(self, image, x,y):
        self.image = image
        self.rect = self.image.get_rect(
            center = (x,y))
        self.is_clicked = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_click(self):
        clicked = False
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            self.image.set_alpha(80)
            if pygame.mouse.get_pressed()[0] and not self.is_clicked:
                clicked = True
                self.is_clicked = True
            elif not pygame.mouse.get_pressed()[0]:
                self.is_clicked = False
        else:
            self.image.set_alpha(255)

        return clicked