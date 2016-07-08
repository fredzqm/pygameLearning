import pygame
import GraphicsUtil as Graph


x = 0
y = 0
img = Graph.heroSprite

# update the game
def updateGame():
    global x, y
    x += 1
    y += 1


# A method that does all the drawing for you.
def draw(screen):
    # setup a differnt background, 
    screen.fill(Graph.BLACK)
    # copy the image of hero to the screen at the cordinate of hero
    screen.blit(img, (x, y))
    
