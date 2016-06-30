import pygame
import GraphicsLib as GLib
import random
from Util import *

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
        hero.vx = 0
        hero.vy = 0

    # update the position of hero based on its speed
    def update(hero):
        hero.x += hero.vx
        hero.y += hero.vy
        bounceIn(hero, 0, 0, 500, 500)

# a greate example for an object that does animation
class Star:
    def __init__(star, x, y, time):
        star.x = x
        star.y = y
        star.birthTime = time

    def update(self, time):
        self.x += 1
        self.y += 1
        showAnimationOn(self, GLib.shiningAnimation, (time - self.birthTime) / 2)
        wrapAroundIn(self, 20, 20, 480, 480)


class Game:
    def __init__(game):
        # initialize the timer and state timer to zero.
        ## game.timer is a clock that record how many ticks has elapsed
        ## game.stateTimer is a clock that record how many ticks has elapsed since switched to this state      
        game.timer = game.stateTimer = 0
        # set the initial background of the game
        game.background = GLib.background
        # set the initial state of game to be "Normal"
        game.state = "Normal"
        
        # put hero as an attribute of the game
        game.hero = Hero()
        game.ball = Object(250, 250, GLib.someLoadedImage)
        game.stars = []
        # put all objects that will be drawn on the screen in a list
        game.objectsOnScreen = [game.hero, game.ball]

    def inState(game, checkedFor):
        return game.state == checkedFor 

    def switchState(game, newState):
        # configure the game when state swiched
        if newState == "Normal":
            game.background = GLib.background
            game.objectsOnScreen = [game.hero, game.ball]
        elif newState == "Pause":
            game.background = GLib.BLACK
            game.objectsOnScreen = [game.hero, game.stars]
        
        # reset the stateTimer when switching to a new state
        game.stateTimer = 0
        game.state = newState


    # updateGame() is called before each frame is displayed
    def updateGame(game):
        # update both the timer and state timer
        game.timer += 1
        game.stateTimer += 1
        # check what state the game is at
        if game.state == "Normal":
            # update the game before each frame of the state
            game.hero.update()
            # dectect collision of stars and hero using rectangle
            for s in game.stars:
                if hasCollideRect(game.hero, s):
                    game.stars.remove(s)
            # showAnimationOn() takes three argument, the object, the animation, and the frameNumber
            # the animation should be a list of surface representing each frame
            # it returns whether a complete animation is shown
            done = showAnimationOn(game.ball, GLib.shiningAnimation, game.stateTimer)
            if done:
                game.switchState("Pause")
        elif game.state == "Pause":
            for s in game.stars:
                s.update(game.timer)
            if game.stateTimer > 30:
                game.switchState("Normal")
        else:
            raise Exception("Undefined game state " + str(state))

    # an example of adding an object to the screen
    def addAnRandomBall(game):
        addedStar = Star(random.randint(0, 500),random.randint(0, 500), game.timer)
        game.stars.append(addedStar)


    # A method that does all the drawing for you.
    def draw(game, screen):
        # set the background of the game
        if type(game.background) is tuple:
            screen.fill(game.background)
        else:
            screen.blit(game.background, (0, 0))

        # the magic that draw all the objects stored in objectsOnScreen onto the screen
        stack = [game.objectsOnScreen]
        while len(stack) > 0:
            objectsLs = stack.pop()
            for obj in objectsLs:
                if type(obj) is list:
                    stack.append(obj)
                else:
                    screen.blit(obj.img, (obj.x, obj.y))


