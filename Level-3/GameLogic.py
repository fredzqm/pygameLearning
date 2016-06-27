import pygame
import GraphicsLib as GLib

# the minimum class for an object that can be displaced on the screen
class ImageObject:
    def __init__(ball, x, y, img):
        ball.x = x
        ball.y = y
        ball.img = img


class Game:
    def __init__(game):
    	# put hero as an attribute of the game
        game.hero = ImageObject(0, 0, GLib.heroSprite)
    

    # updateGame() is called before each frame is displayed
    def updateGame(game):
        # update the position of hero based on its velocity
        game.hero.x += 1
        game.hero.y += 1


    # A method that does all the drawing for you.
    def draw(game, screen):
        # clear the screen, or set up the background, 
        screen.fill(GLib.BLACK)
        # copy the image of hero to the screen at the cordinate of hero
        screen.blit(game.hero.img, (game.hero.x, game.hero.y))


