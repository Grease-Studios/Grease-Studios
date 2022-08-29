def hangman():

    #Imports
    import random

    #User Interface
    print('HANGMAN GAME\n')
    print('-' * 65, ' \n')
    print('Rules Of The Game :\n','You will be given a word to guess.\n',
          'You will have 5 lives that if exhausted will result in a loss.\n',
          'The categories of the words vary between Animals, Occupations and Gadgets.\n',
          'Best of Luck !\n')
    print('-' * 65, ' \n')

    #Inputs and Variables
    player_name = str(input('Enter Player Name : '))
    print('\nWelcome ',player_name,' !\n')

    wordbank = ["hippopotamus","hamster","dolphin","seal","zebra",
                "detective","accountant","thief","blacksmith","jeweler",
                "headphone","radio","remote","computer","keyboard"]

    life = 10
    unseen = {n for n in "abcdefghijklmnopqrstuvwxyz"}
    word = random.choice(wordbank)
    current = ["_" for n in range(len(word))]

    #Main Loop
    while life > 0:

        #Print Status and Check Win
        print(''.join(current), '\n', '-' * 65)
        if '_' not in current:
            print('\n***You Win***\n', '-' * 65)
            break

        #Guess Input
        guess = input('\nGuess a Letter : ').lower()
        while guess not in unseen:
            print('Enter a Valid Letter')
            guess = input('\nGuess a Letter : ').lower()
        unseen.remove(guess)

        #Remaining Letters
        for i, letter in enumerate(word):
            if letter == guess:
                current[i] = letter

        #Life Reduction
        if guess not in word:
            life -= 1
            print('\nWrong', '\n', life, 'live(s) left\n')
            if life == 0:
                print("The correct word is :", word)
                print('\n***You Lose***', '\n', '-' * 65)
                break