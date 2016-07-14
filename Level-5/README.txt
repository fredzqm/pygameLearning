1. Configure game state when switching
2. Build fancy and smooth animation with a template function
3. Manipulate graphics object groups on the screen

=================================================================================
Lesson
=================================================================================
1. Configure game state when switching
	You might want to display different background or objects in different state.
	You might want to have the game stay in a state for a specific amount of time

	To achieve those, you can use a method instead of single assignment to switch state.
		switchState(self, newState):
	Whenever you switch to a new state, you can specify the background and the graphics object group you want to show on the screen.
	It also resets the self.stateTime to zero, which represents how long game has stayed in this state


2. Build fancy and smooth animation with a template function
	You might want to create smooth and continual animation. However, drawing each frame out can be very tedious.
	You can use a template function to create an surface frame and append it to the animation.
	The template function can accept parameters that customizes each frame.
	In this fashion, you can reuse the code and create wonderful animiation easily.

3. Manipulate graphics object groups on the screen
	You might want to suddenly remove and add all stars at once, but removing each of them from the self.objectsOnScreen requires a loop and is error prone.

	In this level, self.objectsOnScreen is a list of graphics objects and list of graphics objects. 
	A whole list of stars can be added to and removed from self.objectsOnScreen in one line.
	You can manipulate graphics objects in groups (similar to Sprite Group)

=================================================================================
Challenge
=================================================================================
