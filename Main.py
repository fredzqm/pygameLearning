#-------------------------
# initialize pygame
#-------------------------
import pygame

# initialize pygame
pygame.init()

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
        if event.type == pygame.QUIT:
            # if someone tries to close the Windows
            exit()
        # check for some key presses
        if event.type == pygame.KEYDOWN:
            print("Button " + str(event.key) + " pressed!")
        elif event.type == pygame.KEYUP:
            print("Button " + str(event.key) + " released!")
        elif event.type == pygame.MOUSEBUTTONDOWN:
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
    pygame.time.wait(100)
    # delay the time, so can see the Windows, controls the frame rate
    