import sys
treasure_image="""
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|
"""
treasure_image2 = ('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /________________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______//______/
*******************************************************************************''')
fire_image = """

               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
wrong_door_image = """
          ________
             / ______ \ 
             || _  _ ||
             ||| || |||
             |||_||_|||
             || _  _o|| (o)
             ||| || |||
             |||_||_|||      ^~^  ,
             ||______||     ('Y') )
            /__________\    /   \/
    ________|__________|__ (\|||/) _________
           /____________\ 
           |____________|
"""
monster_image = """

                            /\_/\
                        /\  |6 6|  /\
                       /  \ \<">/ /  \
                      / ,__`~)-(~___, \
                     /.',-'`/_/`'-,  '.\
                      ,'    \_\    ',
                     :       \|\     ;
                      ',     /|/    ,'
                        '-,__\W\_,-))
                                  ((
                                   )
"""
hole_image = """
      SSSSSSSSSS
      SSSSSSSSSS
.ss.  SSSP""YSSS
SSSS  SSS    SSS
`SS'  SSS.  .SSS
      SSSSSSSSSS
      SSSSSSSSSS
"""
print(treasure_image)
print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")
road = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\": ").lower()
if road == 'left':
    boat = input("""You come to a lake. There is an island in the middle of the lake. Type \"wait\" 
    to wait a boat. Type \"swim\" to swim acroos""").lower()
    if boat == 'wait':
        print("You across the lake and you find a castle at the beach with 3 colored doors")
        door = input("Which door do you choose? (red/blue/yellow)").lower()
        if door == 'yellow':
            print(treasure_image)
            print("You win the game!!")
        elif door == "blue":
            print(wrong_door_image)
            print("It's a room full of fire")
            print("GAME OVER.")
            sys.exit()
        elif door == "red":
            print("It's a room full of fire")
            print(fire_image)
            print("GAME OVER.")
            sys.exit()
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("""
        
        """)
        print("You get attacked by an angry monster. Game Over.")
        print("GAME OVER.")
        sys.exit()
else:
    print(hole_image)
    print("You fell into a hole. Game Over.")
    print("GAME OVER.")
    sys.exit()