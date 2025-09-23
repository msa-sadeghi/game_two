from pygame.sprite import Sprite

class Energy(Sprite):
    def __init__(self, image, x,y, group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
    