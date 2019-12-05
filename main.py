#!/usr/bin/env python3

##### include #####

import keyboard
import time

import snake

##### variable #####

UP = 1
RIGHT = 2
DOWN = -1
LEFT = -2

##### main #####

game = snake.Snake(30, 20)

game.display()

while(True):

    input1 = 0
    input2 = 0

    #input 1
    if(keyboard.is_pressed('z')):
        input1 = UP

    if(keyboard.is_pressed('d')):
        input1 = RIGHT

    if(keyboard.is_pressed('s')):
        input1 = DOWN

    if(keyboard.is_pressed('q')):
        input1 = LEFT

    #input 2
    if(keyboard.is_pressed('up')):
        input2 = UP

    if(keyboard.is_pressed('right')):
        input2 = RIGHT

    if(keyboard.is_pressed('down')):
        input2 = DOWN

    if(keyboard.is_pressed('left')):
        input2 = LEFT

    if(game.move(input1, input2)):
        break

    time.sleep(0.200)
    game.display()
