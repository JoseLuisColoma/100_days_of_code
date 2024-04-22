sound(True)
def move_2_steps():
    move()
    move()
def move_3_steps():
    move()
    move()
    move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()  
def mov_by_the_block():
    move_3_steps()
    turn_left()
    move_3_steps()
def turn_right_and_move():
    turn_right()
    move()
def street_circuit():
    mov_by_the_block()
    turn_right_and_move()
    turn_right()
    mov_by_the_block()
    turn_right_and_move()
    turn_right()
    mov_by_the_block()
    turn_right_and_move()
    turn_right()
    mov_by_the_block()
street_circuit()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
