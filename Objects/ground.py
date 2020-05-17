import pygame


class Ground:
    def __init__(self, x, y, w, h, image):
        self.x, self.y, self.w, self.h, self.image = x, y, w, h, image
        self.collide = True
        self.collectable = False

        self.topoffset = 0
        self.xoffset = 0

    def draw(self, display):
        display.blit(self.image, (self.x, self.y))

    def update(self, keys):
        pass
