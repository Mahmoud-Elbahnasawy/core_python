def play():
    position = (0 , 0)
    alive = False

    while position:

        if position == (0 , 0):
            print("You are in a maze of twisty passages, all alike.")
        elif position == (1 , 0):
            print("You are on a road in a dark forest. To the north you can see a tower.")
        elif position == (1 , 1):
            print("There is a tall tower here, with no obvious door. A path leads east.")
        else:
            print("There is nothing here..")


        command = input("? ")

        i , j = position
        if command == "N":
            position = (i, j+1)
        elif command == "E":
            position = (i+1 , j)
        elif command == "S":
            position = (i , j-1)
        elif command == "W":
            position = (i-1 , j)
        elif command == "L":
            pass
            position = None
        else :
            print(" i don\'t understand", position)
    print("The game is over", position)







def maze(position):
    print("You are in a maze of twisty passages, all alike.")
    return position

def forest(position):
    print("You are on a road in a dark forest. To the north you can see a tower.")
    return position

def tower(position):
    print("There is a tall tower here, with no obvious door. A path leads east.")
    return position
# we need to refactor the play function so that it works as switch case in other programming languages

def play_refactored():

    position = (0 , 0)
    alive = False
    # the question is, why can't we use print without lambda 
    locations = {
        (0,0) : maze ,
        (0,1) : forest,
        (1,1) : tower
    }

    while position:
        print(f"New position is {position}")
        # as you can see the else statement in the play function can not be handled in the location dictionary
        # but we can use a try and catch block to handle it
        try:
            # the following won't work as you did not add the callable bracket ()
            # locations[position]
            # and to fix it use 
            callable_reference = locations[position]
        except KeyError:
            print("There is nothing here..")
        else : 
            position = callable_reference(position)

        command = input("? ")

        i , j = position
        actions = {
            "N":  (i,j+1), 
            "E":  (i+1,j), 
            "S":  (i,j-1),
            "W":  (i-1,j), 
            "L" : (i,j) 
            }
        try: 
            new_position= actions[command]
        except KeyError:
            position = None
            print(" i don\'t understand", position)
        else:
            position = new_position

    else :
        print("This code only happend when the condition is false.")
    
    print("This code happens if the condition was true or even was false")

play_refactored()