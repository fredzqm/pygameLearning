import pygame
import GraphicsLib as GLib
import random
from Util import showAnimationOn, hasCollideRect

# the minimum class for an object that can be displayed on the screen
class Object:
    def __init__(ball, x, y, img):
        ball.x = x
        ball.y = y
        ball.img = img

# a great example of an object that can move on the screen
class Hero:
    def __init__(hero):
        # ------------------------
        # [REQUIRED PART] for any class that will be drawn on the screen
        # Grab the surface that Graphics people worked very hard on
        hero.img = GLib.heroSprite
        # Set the initial coordinate of this object
        hero.x = 0
        hero.y = 0
        # ------------------------
        # TODO: add more properties to Hero based on your game
        hero.vx = 0
        hero.vy = 0

    # update the position of hero based on its speed
    def update(hero):
        hero.x += hero.vx
        hero.y += hero.vy


class Game:
    def __init__(game):
        # initialize the timer to zero.
        # game.timer is a clock that record how many ticks has elapsed
        game.timer = 0
        # set the initial background of the game
        game.background = GLib.BLACK
        # set the initial state of game to be "Normal"
        game.state = "Normal"

        # put hero as an attribute of the game
        game.hero = Hero()
        game.ball = Object(250, 250, GLib.someLoadedImage)
        game.stars = []
        # put all objects that will be drawn on the screen in a list
        game.objectsOnScreen = [game.hero, game.ball]


    # updateGame() is called before each frame is displayed
    def updateGame(game):
        game.timer += 1
        # check what state the game is at
        if game.state == "Normal":
            # update the game before each frame of the state
            game.hero.update()
            # dectect collision of stars and hero using rectangle
            for s in game.stars:
                if hasCollideRect(game.hero, s):
                    game.stars.remove(s)
                    game.objectsOnScreen.remove(s)
            # showAnimationOn() takes three argument, the object, the animation, and the frameNumber
            # the animation should be a list of surface representing each frame
            showAnimationOn(game.ball, GLib.animation, game.timer / 6)
        elif game.state == "Pause":
            pass
        else:
            raise Exception("Undefined game state " + str(game.state))
        return game.state

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


