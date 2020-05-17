import pygame
from Modules.spriteSheet import SpriteSheet


class Kiwi:
    def __init__(self, x, y, w, h, image):
        self.x, self.y, self.w, self.h, self.image = x, y, 64, 64, image  # These are smaller so we make them 64x64
        self.collide = True
        self.collectable = True
        self.collected = False
        self.topoffset = 18
        self.xoffset = 19

        self.idle_length = 17
        kiwi_idle = SpriteSheet(pygame.image.load("./Assets/Collectables/kiwi.png"))
        self.idle = [kiwi_idle.getimage(32 * x, 0, 32, 32) for x in range(self.idle_length)]
        self.idle_state = 0

        self.delay = 2
        self.currDelay = 0

        self.death_length = 6
        kiwi_death = SpriteSheet(pygame.image.load("./Assets/Collectables/collected.png"))
        self.death = [kiwi_death.getimage(32 * x, 0, 32, 32) for x in range(self.death_length)]
        self.death_state = 0

        self.d_delay = 2
        self.d_currDelay = 0

    def draw(self, display):
        if not self.collected:
            display.blit(pygame.transform.scale(self.idle[self.idle_state % self.idle_length],
                                                         (self.w, self.h)), (self.x, self.y))
            if self.currDelay == self.delay:
                self.idle_state += 1
                self.currDelay = 0
            else:
                self.currDelay += 1
        else:  # Play death animation once
            if self.death_state <= self.death_length:
                display.blit(pygame.transform.scale(self.death[self.death_state % self.death_length],
                                                    (self.w, self.h)), (self.x, self.y))

                if self.d_currDelay == self.d_delay:
                    self.death_state += 1
                    self.d_currDelay = 0
                else:
                    self.d_currDelay += 1

    def update(self, keys):
        pass
