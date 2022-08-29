def tic_tac_toe():

    #Import Modules
    import random

    #Global Inputs
    board = [[0,1,2],[3,4,5],[6,7,8]]
    lst = [0,1,2,3,4,5,6,7,8]

    #User Interface
    print('TIC TAC TOE GAME\n')
    print('-' * 65,' \n')

    print('Rules Of The Game :\n','You will play vs an AI in a match of Tic-Tac-Toe.\n',
          'You will get the first turn and the AI will follow next.\n',
          'Your symbol will be X.\n',
          'You will get a grid with boxes labelled 1 to 9 to choose from.\n',
          'Best of Luck !\n')
    print('-' * 65,' \n')

    player_name = str(input('Enter Player Name : '))
    print('\nWelcome ',player_name,' !\n')
    print('-' * 65,' \n')

    #Layout of the Grid of the Game
    def display_grid():

        for i in board:
            for j in i:
                print('|',j,'|', end = "  ")
            print()
        print(' \n')


    #For Player Move
    def player_move():
        box = ""
        while not box.isnumeric() or int(box) not in lst:
            box = input("Please select a Box from "+str(lst)+" : ")
        box = int(box)
        lst.remove(box)
        board[box//3][box%3] = 'X'
        display_grid()


    #For AI Move
    def ai_move():

        indx = random.choice(lst)
        lst.remove(indx)
        board[indx//3][indx%3] = 'O'
        print('\nThe AI chose Box '+str(indx)+' : ')
        display_grid()


    #Check Win Condition
    def check_win():
        for p in ('X','O'):

            #horizontal check
            if any(set(board[i]) == {p} for i in range(3)):
                print('***Great Job !***\n'+'***You Win***\n'+'-' * 65, ' \n' if p == 'X' else '***Good Luck Next Time.***\n'+'***AI Wins***\n'+'-' * 65, ' \n')
                return True

            #vertical check
            if any(set([board[0][i], board[1][i], board[2][i]]) == {p} for i in range(3)):
                print('***Great Job !***\n'+'***You Win***\n'+'-' * 65, ' \n' if p == 'X' else '***Good Luck Next Time.***\n'+'***AI Wins***\n'+'-' * 65, ' \n')
                return True

            #diagonal check
            if set([board[0][0],board[1][1],board[2][2]]) == {p} or set([board[0][2],board[1][1],board[2][0]]) == {p}:
                print('***Great Job !***\n'+'***You Win***\n'+'-' * 65, ' \n' if p == 'X' else '***Good Luck Next Time.***\n'+'***AI Wins***\n'+'-' * 65, ' \n')
                return True

    #To determine one turn cycle
    def turn():
        player_move()
        if check_win():raise Exception()
        ai_move()
        if check_win():raise Exception()
        print('-' * 65,' \n')

    #Main Code
    def game():
        print('Play Grid : \n')
        display_grid()
        print('-' * 65,' \n')
        turn()
        turn()
        turn()
        turn()
        player_move()
        if check_win():raise Exception()
        print('***Tie***')
        print('-' * 65,' \n')

    try:
        game()
    except:
        return