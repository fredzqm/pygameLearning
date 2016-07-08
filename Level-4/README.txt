Use object-oriented programming

=================================================================================
Lesson
=================================================================================
1. Use class to represent an object on the screen
	Notice that any object on screen needs two information
		how it looks like (img  / its surface)
		where it locates  (x, y / its coordinate)

	In object-oriented programming, we store those information closely related to an object as its attribute.
	We use class ImageObject that contains the minimun attributes that are required to be put on the scree.
		To create an instance of ImageObject, you need to pass in the initial value of those attributes					hero = ImageObject(x, y, img)
		To modify the attribute of this instance, you can assign to those attributes									hero.x = x_position

	You can create your own class to represent any customized objects on the screen, as long as them have three required attributes (x, y, img)
	As the game grows larger, you can even separate those classes into several different files.

2. Use class to represent the whole game.
	All parts of the state of the game should be attributes of the game.
		As in the example, hero is a part of the game, so we stores it in an attribute of game -- self.hero

	Game class has three important methods:
		__init__(self):	 		
			What is it?			This is the constructor of the game.
			Where we use it?	Just above the main while loop, we creates an instance of the game
			What goes in there?	The initialization of the Game, such as initial game state, initial hero position
								It grows fast as you add more features to your game

		updateGame(self):		
			What is it?			This is the game logic of the game.
			Where we use it?	We call this method before we update each frame inside main while loop
			What goes in there? Dynamic game logic, such as moving, animiation, collision, state transition
								It grows really fast as you add more complex logic

		draw(self, screen):		
			What is it?			This is the graphics block of the game
			Where we use it?	We call this method after we update the state of the game
			What goes in there? Copying images of objects to the screen


=================================================================================
Challenge
=================================================================================
1. use ImageObject to add static  
