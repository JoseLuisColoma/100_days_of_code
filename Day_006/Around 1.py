sound(True)
def move_2_steps():
    move()
    move()
def move_9_steps():
    for i in range(9):
        move()
        put()
def turn_right():
    turn_left()
    turn_left()
    turn_left()  
def street_and_turn():
    move_9_steps()
    turn_left()
def around():    
    for i in range(4):
        street_and_turn()
around()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
