def stone_paper_scissor():

    #Import Module
    import random

    #User Interface
    print("STONE PAPER SCISSORS\n")
    print('-' * 65, ' \n')
    print("Rules of the Game :\n","You will face an AI in a game of Stone Paper Scissors.\n",
          "You will have 3 options to choose from.\n","Best of Luck !\n")
    print('-' * 65, ' \n')

    player_name = str(input('Enter Player Name : '))
    print('\nWelcome ', player_name, ' !\n')
    print('-' * 65, ' \n')

    print("Choice of Inputs :\n",
          "1 : Stone\n",
          "2 : Paper\n",
          "3 : Scissors\n")
    print('-' * 65, ' \n')

    #Inputs and Variables
    a = {1: 'Stone', 2: 'Paper', 3: 'Scissors'}
    p = int(input("Enter Choice : "))
    while p < 1 or p > 3:
        p = int(input("Enter Valid Choice : "))

    y = random.randint(1,3)

    #Functions
    def result():
        if p == y:
            print("*** Tie ***")
        elif p == 1 and y == 2:
            print("*** AI Wins ***")
        elif p == 2 and y == 1:
            print("*** You Win ***")
        elif p == 1 and y == 3:
            print("*** You Win ***")
        elif p == 3 and y == 1:
            print("*** AI Wins ***")
        elif p == 2 and y == 3:
            print("*** AI Wins ***")
        elif p == 3 and y == 2:
            print("*** You Win ***")

    #Main Loop
    print("\nYour Action:",a[p],"\n")
    print("AI Action:",a[y],"\n")
    result()
    print('-' * 65, ' \n')