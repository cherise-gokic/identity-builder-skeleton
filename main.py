""" Identity Collector Game (skeleton code)

Collect 12 identity pieces to fill your character before time runs out
"""

scene.set_background_color(3)

long_text = "How to play: You must build up the person by gathering their identities."
game.show_long_text(long_text, DialogLayout.BOTTOM)
key = "The star stands for [insert identity here]. The rose stands for [insert identity here]. The diamond stands for [insert identity here]. The heart stands for [insert identity here]. "
game.show_long_text(key, DialogLayout.BOTTOM)

# Day 5 -- insert code here: create your character and set it as a player

# Day 6 -- insert code here: set the starting position of the character

# Day 6 -- insert code here: set the controls to move the character side to side

# Day 6 -- insert code here: make the character stay in the screen

info.start_countdown(15)


def on_update_interval():
    """
    Every 1000 ms, generate an identity piece that moves down the screen
    """

    # Day 5 -- insert code here: create identity image and store it in a variable

    # Day 5 -- insert code here: create identity image and store it in a variable

    # Day 5 -- insert code here: create identity image and store it in a variable
    
    # Day 7 -- insert code here: create list of identity sprite images

    # Day 7 -- uncomment the code below:
    # identityNum = randint(0, len(identityList) - 1)

    # Day 7 -- insert code here: create projectile sprite from randomly selected identity image

    # Day 7 -- uncomment the code below:
    # projectile.x = randint(0, scene.screen_width())
game.on_update_interval(1000, on_update_interval)

def on_overlap(sprite, otherSprite):
    """
    Called when character and identity piece touch
    - Increase score by 1
    - Update image of character as score increases
    - Win game when score reaches 12
    """
    # Day 8 -- insert code here: increase score by 1
    
    # Day 8 -- uncomment the code below:
    # otherSprite.destroy()
    if info.score() == 2:
        sprite.set_image(img("""
            . . . . f f f f . . . . .
            . . f f f f f f f f . . .
            . f f f f f f c f f f . .
            f f f f f f c c f f f c .
            f f f c f f f f f f f c .
            c c c f f f e e f f c c .
            f f f f f e e f f c c f .
            f f f b f e e f b f f f .
            . f 4 1 f 4 4 f 1 4 f . .
            . f e 4 4 4 4 4 4 e f . .
            . f f f e e e e f f f . .
            . . . . . . . . . . . . .
            . . . . . . . . . . . . .
            . . . . . . . . . . . . .
            . . . . . . . . . . . . .
            . . . . . . . . . . . . .
            """))
    
    # Day 8 -- insert code here: when character has 4 identity pieces, update character image

    # Day 8 -- insert code here: when character has 6 identity pieces, update character image

    # Day 8 -- insert code here: when character has 8 identity pieces, update character image

    # Day 8 -- insert code here: when character has 10 identity pieces, update character image

    # Day 8 -- insert code here: when character has 12 identity pieces, update character image to complete character, pause to see full character, and win the game
    
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_overlap)
