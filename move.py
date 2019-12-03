import mm_main


directions = ['north', 'south', 'east', 'west']


def movement():
    response = input("Input the direction you wish to travel (north / south / east / west)\n")
    if response == 'north':
        print("You move north.\n")
        mm_main.main()
    
    elif response == 'south':
        print("You move south.\n")
        mm_main.main()
    
    elif response == 'east':
        print("You move east.\n")
        mm_main.main()
    
    elif response == 'west':
        print("You move west.\n")
        mm_main.main()
    
    else:
        print("I didn't understand that.\n")
        movement()