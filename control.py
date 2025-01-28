from pynput.mouse import controller
from pynput.keyboard import controller

def controlMouse() : 
mouse = controller()
mouse.position = (10,20)
#(left to right,top to bottom)

def controlKeyboard() : 
keyboard = controller()
keyboard.type('I am freaking Awsome')
controlKeyboard()
