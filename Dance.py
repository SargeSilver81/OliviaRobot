# template_file.py
# This file should form the starting block to any script for the Pi Robot

# Import Python elements
from rrb3 import *
import sys
import tty
import termios

# Set any aliases
rr = RRB3(9.0, 6.0) # (battery, motor)

# Commands
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

# Set Default Exit Massage or Instructions
print("Press CTRL-c to quit the program")

# The Code goes below here
