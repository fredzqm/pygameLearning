import pygame
import GraphicsUtil as Graph

# the minimum class for an object that can be displaced on the screen
class ImageObject:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img


class Game:
    def __init__(self):
    	# put hero as an attribute of the game
        self.hero = ImageObject(0, 0, Graph.heroSprite)
    

    # updateGame() is called before each frame is displayed
    def updateGame(self):
        # update the position of hero based on its velocity
        self.hero.x += 1
        self.hero.y += 1


    # A method that does all the drawing for you.
    def draw(self, screen):
        # clear the screen, or set up the background, 
        screen.fill(Graph.BLACK)
        # copy the image of hero to the screen at the cordinate of hero
        screen.blit(self.hero.img, (self.hero.x, self.hero.y))


