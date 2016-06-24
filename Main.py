    #-------------------------
# initialize pygame
#-------------------------
import pygame
# initialize pygame
pygame.init()

# create a screen of 500 * 500
screen = pygame.display.set_mode((500, 500))

# <<ADVANCED>> If you want KEYDOWN event to fire continuously, when a key is held down
# ============ give it two argument, both of them are interval of KEYDOWN event
pygame.key.set_repeat(50, 50)

#-------------------------
# initialize the game
#-------------------------
# import the game class from GameLogic
from GameLogic import Game, GLib

# acquire a game object
game = Game()

# Let "Normal" be the initial state
state = "Normal"

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
            # control the hero velocity
            if event.key == pygame.K_UP:
                game.hero.vy -= 3
            elif event.key == pygame.K_DOWN:
                game.hero.vy += 3
            elif event.key == pygame.K_LEFT:
                game.hero.vx -= 3
            elif event.key == pygame.K_RIGHT:
                game.hero.vx += 3
            # change the background color
            elif event.key == pygame.K_o:
                game.background = GLib.ORANGE
            elif event.key == pygame.K_b:
                game.background = GLib.BLACK
            # add an random ball to the screen
            elif event.key == pygame.K_a:
                game.addAnRandomBall()
            # reset the position or velocity of hero
            elif event.key == pygame.K_p:
                game.hero.x = 200
                game.hero.y = 200
            elif event.key == pygame.K_s:
                game.hero.vx = 0
                game.hero.vy = 0
        # click on the screen to toggle state
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if state == "Normal":
                state = "Pause"
            else:
                state = "Normal"
    #-------------------------
    # The main game logic block
    #-------------------------
    ## all the exciting interactive of objects happen in updateGame()
    state = game.updateInState(state)
    # update both timer and stateTimer, if the state changed, clear the stateTimer
    game.timer += 1
    
    #-------------------------
    # The graphics block
    #-------------------------
    ## all the drawing happen in updateGame()
    game.draw(screen)

    #-------------------------
    # display this frame and wait
    #-------------------------
    pygame.display.flip()
    # ask pygame to display everythong on the GUI
    pygame.time.wait(100)
    # delay the time, so can see the Windows, controls the frame rate
    