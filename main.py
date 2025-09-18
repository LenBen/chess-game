import sys

def start_menu() -> None: # The start menu for the chess game
    choice = 3
    while choice != 1 or choice != 2:
        print("This is a two-player chess game, what would you like to do?")
        print("1.Start game\n2.Exit")
        choice = int(input())
        if choice == 2:
            sys.exit()
        elif choice == 1:
            #start game
            print()
        else:
            print("Not a valid answer")


if __name__ == "__main__":
    start_menu()