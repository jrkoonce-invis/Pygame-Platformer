import pygame


class Box:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.collide = True
        self.collectable = False

        self.topoffset = 0
        self.xoffset = 0

    def draw(self, display):
        pygame.draw.rect(display, (0, 0, 0), (self.x, self.y, self.w, self.h))

    def update(self, keys):
        pass
