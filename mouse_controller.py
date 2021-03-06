# Program controls the mouse

# Only problem is figuring out how to draw from edge of screen to mouse

import pyautogui 		# Library to control keyboard and mouse functions
import tkinter			# Library/toolkit for updating laptop screen

print("Press Ctrl-C to quit.")

pyautogui.PAUSE = 2.5		# Gives 2.5 second pause before running the program again

pyautogui.FAILSAFE = True 	# Failsafe termination after moving mouse to upper left corner of the screen

while True:

	except KeyboardInterrupt:
		print("Done\n")
		break
	# Calculate x and y of the mouse
	x_coordinate = pyautogui.position().x
	y_coordinate = pyautogui.position().y
	coordinate = (x_coordinate, y_coordinate)

	# Calculate the x and y max length of screen
	x_screenmax = pyautogui.size().width
	y_screenmax = pyautogui.size().height
	screensize = (x_screenmax, y_screenmax)
	# Track mouse along screen border
	track_x = (x_coordinate, 0)
	track_y = (0, y_coordinate)

	# Draw lines from border to mouse


	print(coordinate)		# Prints mouse coordinates to terminal

	print(screensize)		# Print screen size to terminal

	# The end= prevents default newline character from being added to end of printed line
	print(positionStr, end=" ")

	# The \b escapes the characters and with flush prints new text
	print('\b' * len(positionStr), end=" ", flush=True)
