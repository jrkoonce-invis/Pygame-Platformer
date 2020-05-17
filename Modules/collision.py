from Objects.kiwi import Kiwi


def player_check(player, obj):

    xoffset = 8 + obj.xoffset  # Helps with sprite size issues (b/c homemade collision system)
    yoffset = 10  # Helps with sprite size issues (b/c homemade collision system)

    topoffset = obj.topoffset  # Special for neccessary changes sprite

    # Player Horizontal Collision
    if player.x + xoffset < obj.x + obj.w and player.x + player.w - xoffset > obj.x \
            and player.last_y + player.h > obj.y + topoffset and player.last_y < obj.y + obj.h - yoffset and \
            (player.state == "RUN_LEFT" or (player.state == "JUMP" and player.pastState == "RUN_LEFT")):
        if obj.collectable:
            obj.collected = True
        else:
            player.x = obj.x + obj.w - xoffset
    elif player.x + player.w - xoffset > obj.x and player.x + xoffset < obj.x + obj.w \
            and player.last_y + player.h > obj.y + topoffset and player.last_y < obj.y + obj.h - yoffset and \
            (player.state == "RUN_RIGHT" or (player.state == "JUMP" and player.pastState == "RUN_RIGHT")):
        if obj.collectable:
            obj.collected = True
        else:
            player.x = obj.x - player.w + xoffset

    # Player Vertical Collision (Gravity stuff)
    if player.y + player.h >= obj.y + topoffset and player.y < obj.y + obj.h - yoffset \
            and player.x + xoffset < obj.x + obj.w \
            and player.x + player.w - xoffset > obj.x and player.state == "JUMP":
        if obj.collectable:
            obj.collected = True
        else:
            player.y = obj.y + obj.h - yoffset
            player.isOnGround = False
            player.jumpVel = 0
            player.currG = 0
    elif player.y + player.h >= obj.y + topoffset and player.y < obj.y + obj.h - yoffset \
            and player.x + xoffset < obj.x + obj.w \
            and player.x + player.w - xoffset > obj.x:
        if obj.collectable:
            obj.collected = True
        else:
            player.y = obj.y - player.h + topoffset
            player.gs += 1
            player.isOnGround = True
