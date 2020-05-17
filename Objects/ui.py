import pygame


class Ui:
    def __init__(self, x, y, w, h, image):
        self.x, self.y, self.w, self.h, self.image = x, y, w, h, image

    def draw(self, display):
        display.blit(pygame.transform.scale(self.image, (self.x, self.y)), (self.x, self.y))

    def update(self, keys):
        pass

    def clicked(self, pos):
        x, y = pos
        if self.x + self.w > x > self.x and self.y < y < self.y + self.h:
            return True
        else:
            return False

    def activate(self):
        pass


class StartButton(Ui):
    def activate(self):
        return "start game"
