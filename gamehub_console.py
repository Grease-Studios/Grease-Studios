#Imports
import time
import sps_v2
import tictactoe_v3
import hangman_v2

#Functions
def interface():
    print("\n",'-' * 65,'\n',
          "\nGAME HUB\n",
          "\nWelcome to Gamehub !\n",
          "\nMade by : Pranav, Daiyan and Ipshita","\nClass 12-A, Shalom Hills International School\n",
          '\n','-' * 65,
          "\nYou may select your game of preference from the list below.\n",
          "1 : Stone Paper Scissors\n",
          "2 : Tic Tac Toe\n",
          "3 : Hangman\n",
          "4 : Exit\n",
          '-' * 65)

#Main Loop
while True:

    time.sleep(1)
    interface()

    x = int(input("\nEnter Number For The Game Of Choice : "))
    while x < 1 or x > 4:
        x = int(input("\nEnter Number For The Game Of Choice : "))
    print('-' * 65, ' \n')

    if x == 1:
        sps_v2.stone_paper_scissor()

    elif x == 2:
        tictactoe_v3.tic_tac_toe()

    elif x == 3:
        hangman_v2.hangman()

    elif x == 4:
        print("Thank You For Playing !")
        print('-' * 65)
        break