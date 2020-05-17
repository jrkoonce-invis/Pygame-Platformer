import pygame
from Objects.player import Player
from Objects.kiwi import Kiwi
from Objects.ground import Ground
from Objects.background import Background
from Objects.box import Box
from Modules.collision import *
from pytmx.util_pygame import load_pygame
from Modules.camera import Camera
from Objects.ui import *

pygame.init()

display_width = 32 * 20
display_height = 32 * 20

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
done = False

objects = []
elements = []
gameState = 1

# UI Start Button
elements.append(StartButton(100, 100, 64, 64, pygame.image.load("./Assets/UI/play.png")))

# Main Player
player_x = 0
player_y = 0
player_width = 64
player_height = 64
objects.append(Player(player_x, player_y, player_width, player_height))

# Left Wall + Right Wall
objects.append(Box(-10, 0, 10, display_height))
objects.append(Box(32 * 40, 0, 10, display_height))

# Tiled and Pytmx
tiled_map = load_pygame('./Assets/Levels/BasicLevel.tmx')
for layer in tiled_map.visible_layers:
    for x, y, image, in layer.tiles():
        if layer.name == "Background":
            objects.append(Background(x * tiled_map.tilewidth, y * tiled_map.tileheight,
                                      tiled_map.tilewidth, tiled_map.tileheight, image))
        elif layer.name == "Terrain":
            objects.append(Ground(x * tiled_map.tilewidth, y * tiled_map.tileheight,
                                  tiled_map.tilewidth, tiled_map.tileheight, image))
        elif layer.name == "Collectibles":
            objects.append(Kiwi(x * tiled_map.tilewidth, y * tiled_map.tileheight,
                                tiled_map.tilewidth, tiled_map.tileheight, image))

# Camera
camera = Camera(32 * 40)


while not done:

    clock.tick(60)
    keys = pygame.key.get_pressed()

    event = pygame.event.get()

    for e in event:
        if e.type == pygame.QUIT:
            done = True

    if gameState == 2:  # PLay Game

        # Update
        display.fill((0, 0, 0))
        for obj in objects:
            obj.update(keys)

        # Camera
        while camera.check(objects[0], display_width, display_height):
            for obj in objects:
                camera.movecamera(obj)

        # Collision
        for obj in objects:
            if not isinstance(obj, Player) and obj.collide:
                # objects[0] is always the player
                player_check(objects[0], obj)

        # Draw
        for obj in objects:
            if not isinstance(obj, Player):
                obj.draw(display)
        objects[0].draw(display)

    elif gameState == 1:
        for ele in elements:
            ele.draw(display)

        for e in event:
            if e.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for u in elements:
                    if u.clicked(pos):
                        if u.activate() == "start game":
                            gameState = 2

    pygame.display.flip()
