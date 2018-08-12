# template_file.py
# This file should form the starting block to any script for the Pi Robot

# Import Python elements
from rrb3 import *
import sys
import tty
import termios

# Set any aliases
rr = RRB3(9.0, 3.0) # (battery, motor)

# Commands
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

# Set Default Exit Massage or Instructions
print("Use the arrow keys to control the robot ")
print("Press CTRL-c to quit the program")

# The Code goes below here

# These functions allow the program to read your keyboard
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows

# This will control the robot 
try:
    while True:
        poppy = readkey()
        if poppy == UP:
            rr.forward(0.5)
            print 'forward'
        elif poppy == DOWN:
            rr.reverse(0.5)
            print 'reverse'
        elif poppy == RIGHT:
            rr.right(0.5)
            print 'right'
        elif poppy == LEFT:
            rr.left(0.5)
            print 'left'
        elif poppy == ' ':
            rr.stop()
            print 'stop'
        elif ord(poppy) == 3:
            break
except KeyboardInterrupt:
    GPIO.cleanup()