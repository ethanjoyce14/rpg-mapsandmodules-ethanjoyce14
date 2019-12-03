import move
import map


def main():
    while True:
        response = ""
        response = input("Please enter a command (move / map / quit)\n")
        if response == 'move':
            move.movement()
        elif response == 'map':
            map.minimap()
        elif response == 'quit':
            quit()
        else:
            print("I didn't understand that.\n")
            main()
    

main()
