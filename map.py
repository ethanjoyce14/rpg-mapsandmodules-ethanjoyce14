import mm_main


def minimap():
    print(r"""
    1 2 3 4 5 6 7 8 9 10       Legend:
  +---------------------+      [ . ] = Grass
A | $ $ = . . . . ^ ^ ^ |      [ # ] = Forest
B | = = . . * * * * ^ ^ |      [ - ] = Road
C | $ = = * " " " " . ^ |      [ " ] = Farm
D | = - - - * " " " " . |      [ * ] = Hedgerow
E | # # . - - * " " " . |      [ ^ ] = Mountain
F | # . - - - - - . . . |      [ = ] = Building
G | - - - . . . - - | | |      [ $ ] = Shop
H | # . # . . . | - | = |      [ | ] = Wall
I | # # $ . | | | = = $ |      
J | # # # # | = $ . $ = |      
  +---------------------+      
    """)
    
    response = input("Type 'back' to go back\n")
    if response == 'back':
        mm_main.main()
    
    else:
        print("I didn't understand that.\n")
        minimap()
