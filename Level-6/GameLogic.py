import pygame
import GraphicsUtil as Graph
import random
from Util import *

# the minimum class for an object that can be displayed on the screen
class ImageObject:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    # the method that should update the status of game depending on the game.
    # Its subclass should overrides it
    def update(self, game):
        pass


# a greate example for an object that does animation
class Star(ImageObject):
    def __init__(self, x, y, time):
        super().__init__(x, y, Graph.shiningAnimation[0])
        self.birthTime = time

    def update(self, game):
        self.x += 1
        self.y += 1
        # dectect collision of stars and hero using rectangle
        if hasCollideRect(game.hero, self):
            game.stars.remove(self)
            return
        showAnimationOn(self, Graph.shiningAnimation, (game.time - self.birthTime) / 2)
        wrapAroundIn(self, 20, 20, 480, 480)


class Ball(ImageObject):
    def update(self, game):
        if showAnimationOn(self, Graph.shiningAnimation, game.stateTime / 5):
            game.switchState("Pause")


class MovingObject(ImageObject):
    def __init__(self, x, y, img, vx, vy):
        super().__init__(x, y, img)
        self.vx = vx
        self.vy = vy
        
# a great example of an object that can move on the screen
# Hero is a subclass of ImageObject so it has l
class Hero(MovingObject):
    def __init__(self):
        super().__init__(0, 0, Graph.heroSprite, 0, 0)

    # this method overrides the 
    def update(self, game):
        self.x += self.vx
        self.y += self.vy
        bounceIn(self, 0, 0, 500, 500)

class Bullet(MovingObject):
    def __init__(self, x, y, img, vx, vy):
        super().__init__(0, 0, Graph.heroSprite, 0, 0)




        

class Game:
    def __init__(self):
        # initialize the time and state time to zero.
        ## self.time is a clock that record how many ticks has elapsed
        ## self.stateTime is a clock that record how many ticks has elapsed since switched to this state      
        self.time = self.stateTime = 0
        # set the initial background of the game
        self.background = Graph.background
        # set the initial state of game to be "Normal"
        self.state = "Normal"
        
        # put hero as an attribute of the game
        self.hero = Hero()
        self.ball = ImageObject(250, 250, Graph.someLoadedImage)
        self.stars = []
        # put all objects that will be drawn on the screen in a list
        self.objectsOnScreen = [self.hero, self.ball]


    def switchState(self, newState):
        # configure the game when state swiched
        if newState == "Normal":
            self.background = Graph.background
            self.objectsOnScreen = [self.hero, self.ball]
        elif newState == "Pause":
            self.background = Graph.BLACK
            self.objectsOnScreen = [self.hero, self.stars]
        
        # reset the stateTime when switching to a new state
        self.stateTime = 0
        self.state = newState


    # an example of adding an object to the screen
    def addAnRandomBall(self):
        addedStar = Star(random.randint(0, 500),random.randint(0, 500), self.time)
        self.stars.append(addedStar)

    
    # updateGame() is called before each frame is displayed
    def updateGame(self):
        # update both the time and state time
        self.time += 1
        self.stateTime += 1
        # check what state the game is at
        if self.state == "Pause" and self.stateTime > 200:
            self.switchState("Normal")

        # a magic that update all elements on the screen for you
        # However, all methods need to implement obj.update(game)
        def updateObj(objls):
            for obj in objls:
                if type(obj) is list:
                    updateObj(obj)
                else:
                    obj.update(self)
        updateObj(self.objectsOnScreen)


    # A method that does all the drawing for you
    def draw(self, screen):
        # set the background of the game
        if type(self.background) is tuple:
            screen.fill(self.background)
        else:
            screen.blit(self.background, (0, 0))

        # the magic that draw all the objects in objectsOnScreen onto the screen
        def drawOnScreen(objls):
            for obj in objls:
                if type(obj) is list:
                    drawOnScreen(obj)
                else:
                    screen.blit(obj.img, (obj.x, obj.y))
        drawOnScreen(self.objectsOnScreen)


