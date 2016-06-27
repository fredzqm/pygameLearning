import pygame
import GraphicsLib as GLib
import random
from Util import hasCollideRect

# the minimum class for an object that can be displayed on the screen
class Object:
    def __init__(ball, x, y, img):
        ball.x = x
        ball.y = y
        ball.img = img


class Game:
    def __init__(game):
        # set the initial background of the game
        game.background = GLib.BLACK
        # put hero as an attribute of the game
        game.hero = Object(0, 0, GLib.heroSprite)
        game.stars = []
        # put all objects that will be drawn on the screen in a list
        game.objectsOnScreen = [game.hero]


    # updateGame() is called before each frame is displayed
    def updateGame(game):
        # dectect collision of stars and hero using rectangle
        for s in game.stars:
            if hasCollideRect(game.hero, s):
                game.stars.remove(s)
                game.objectsOnScreen.remove(s)
                

    # an example of adding an object to the screen
    def addAnRandomBall(game):
        addedStar = Object(random.randint(0, 500),random.randint(0, 500), GLib.someLoadedImage)
        game.stars.append(addedStar)
        game.objectsOnScreen.append(addedStar)


    # A method that does all the drawing for you.
    def draw(game, screen):
        # clear the screen, or set up the background, 
        screen.fill(game.background)

        for obj in game.objectsOnScreen:
            screen.blit(obj.img, (obj.x, obj.y))


