#-------------------------
# initialize pygame
#-------------------------
import pygame

# initialize pygame
pygame.init()

# initialize a clock for the game, so you can control the framerate
clock = pygame.time.Clock()

# create a screen of 500 * 500
screen = pygame.display.set_mode((500, 500))

import GameLogic

#-------------------------
# Our Main Loop
#-------------------------
## Your must have one and only one big while loop for your game
## Each time the loop is executed, one framed
while True:
    #-------------------------
    # Our event hanlding loop
    #-------------------------
    eventList = pygame.event.get()
    # grab all events pygame recieved
    for event in eventList:
        print(event)
        if event.type == pygame.QUIT:
            # if someone tries to close the Windows
            exit()
        # check for some key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space pressed!")
            print("Button " + str(event.key) + " pressed!")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # grab the position coordinate of the mouse
            print("Mouse clicked at " + str(event.pos))

    #-------------------------
    # The main game logic block
    #-------------------------
    ## all the exciting interactive of objects happen in updateGame()
    GameLogic.updateGame()

    #-------------------------
    # The graphics block
    #-------------------------
    ## all the drawing happen in updateGame()
    GameLogic.draw(screen)

    #-------------------------
    # display this frame and wait 
    #-------------------------
    pygame.display.flip()
    # ask pygame to display everythong on the GUI
    
    clock.tick(60)
    # set the framerate of the game to 60fps, i.e. 60 updates in one second
    