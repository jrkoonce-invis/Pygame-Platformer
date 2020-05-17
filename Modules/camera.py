from Objects.player import Player


class Camera:
    def __init__(self, levellength):
        self.speed = 1
        self.x = self.speed
        self.y = 0
        self.xpos = 0
        self.ymax = levellength

    def movecamera(self, obj):
        obj.x -= self.x
        if isinstance(obj, Player):
            if self.x == self.speed:
                self.xpos += self.speed
            else:
                self.xpos -= self.speed

    def check(self, player, w, h):
        if w - 200 < player.x + player.w < self.ymax - self.xpos - 200:
            self.x = self.speed
            return True
        elif player.x < 200 and self.xpos > 0:
            self.x = -self.speed
            return True
        else:
            return False
