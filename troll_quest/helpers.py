
#The Starting menu of the game
def start_menu():
    print('Welcome to Troll Quest')
    print('Choose your option')
    print('1 - New Game')
    print('q - Quit Game')
    startgame = 0
    while startgame != "1" and startgame != "q":
        startgame = input("Enter 1 or q: ")
        if startgame == "1":
            intro_screen()
    return startgame

#Intro Screen
def intro_screen():
    print("Welcome to the Cave!")
