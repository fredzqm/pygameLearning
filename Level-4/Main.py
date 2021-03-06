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

# <<ADVANCED>> If you want KEYDOWN event to fire continuously, when a key is held down
# ============ give it two argument, both of them are interval of KEYDOWN event
pygame.key.set_repeat(50, 50)

#-------------------------
# initialize the game
#-------------------------
# import the game class from GameLogic
from GameLogic import Game, Graph

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
                game.hero.vy -= 0.5
            elif event.key == pygame.K_DOWN:
                game.hero.vy += 0.5
            elif event.key == pygame.K_LEFT:
                game.hero.vx -= 0.5
            elif event.key == pygame.K_RIGHT:
                game.hero.vx += 0.5
            # change the background color
            elif event.key == pygame.K_o:
                game.background = Graph.ORANGE
            elif event.key == pygame.K_b:
                game.background = Graph.BLACK
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
            # toggle normal and puase state
            if game.state == "Normal":
                game.state = "Pause"
            else:
                game.state = "Normal"
    #-------------------------
    # The main game logic block
    #-------------------------
    # all the exciting interactive of objects happen in updateGame()
    game.updateGame()
    
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
        
    clock.tick(60)
    # set the framerate of the game to 60fps, i.e. 60 updates in one second
