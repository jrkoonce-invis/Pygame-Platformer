import pygame


class SpriteSheet:
    def __init__(self, image):
        self.ss = image.convert_alpha()

    def getimage(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.ss, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))

        return image
