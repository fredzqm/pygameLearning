get something moving on the screen
=================================================================================

1. import global variables and global function from another file
	There are essentially two way to import code from a file called "module1.py" in the same directory
		import as a whole module. You can use as to specify a different name for the module
		later on, you need to prefix that name for each access of global variables or functions
			import module1 as mod1
			print(mod1.global_variable_in_module1)
			mod1.global_function_in_module1(...)

		import specific global variable or function directly. No need for prefix
		from module1 import *   is equivalent to copying "module.py" file over
			from module1 import global_variable_in_module1, global_function_in_module1
			print(global_variable_in_module1)
			global_function_in_module1(...)


2. separate program in multiple parts and files
	In a team work, it is a very good practice to keep different part of your game in different file.
	Our pygame program contains three part:
		Main.py (I/O)
			It contains the big main loop, a very structured loop that is run for each frame
			Besides what we have in the previous level, to make the interactive, it needs:
				1. event loop, which handles user input
				2. game logic, which update the game state
				3. graphics block, which draw components to the screen
				4. display on the screen and wait for a interval
			In this example, part 2 and 3 are just calling a function in GameLogic.py

		GameLogic.py
			It only has two simple functions:
				updateGame()		all the complex logic of the game is here.
				draw(screen)		all the drawing is happened here

		GraphicsLib.py
			All the pre-drawn surfaces of sprites should be here.
			GameLogic can then import these sprites for draw(screen)

