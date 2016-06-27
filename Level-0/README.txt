Get something show up on the screen
=================================================================================


pygame.init()
	initialize pygame, so it's ready for work

pygame.display.set_mode((screenWidth, screenHeight))
	creates an surface representing the screen

Color = (Red, Green, Blue)
	creates an tuple of three element to represent color

pygame.draw.circle(surfaceToBeDrawnOn, color, centerCordinate, radius)
	pygame.draw.SomeMethod(surface, ...) can be used to draw premitive figures on screen
	Look up other methods you can use at http://www.pygame.org/docs/ref/draw.html

pygame.display.flip()
	This is the only command that pygame would actually change the GUI screen
	After ploting the surface, let's print it to the screen