#A game of Scissors, paper and stone against the machine

import random

def choice_player2(): #Function with random for the other player, in this case: the machine
    options = ['Scissors', 'Paper', 'Stone']
    random_choice = random.choice(options)
    return random_choice

def play(choice_player1, choice_player2):
        
    print('One two three scissors, paper and stone!')
    if choice_player1 == 'Scissors' and choice_player2 == 'Paper':
        print(f'{choice_player1} against {choice_player2}')
        print('Player 1 wins')
    elif choice_player1 == 'Scissors' and choice_player2 == 'Stone':
        print(f'{choice_player1} against {choice_player2}')
        print('The machine wins')
    elif choice_player1 == 'Scissors' and choice_player2 == 'Scissors':
        print(f'{choice_player1} against {choice_player2}')
        print('It is a draw!')
    elif choice_player1 == 'Paper' and choice_player2 == 'Stone':
        print(f'{choice_player1} against {choice_player2}')
        print('Player 1 wins')
    elif choice_player1 == 'Paper' and choice_player2 == 'Scissors':
        print(f'{choice_player1} against {choice_player2}')
        print('The machine wins')
    elif choice_player1 == 'Paper' and choice_player2 == 'Paper':
        print(f'{choice_player1} against {choice_player2}')
        print('It is a draw!')    
    elif choice_player1 == 'Stone' and choice_player2 == 'Scissors':
        print(f'{choice_player1} against {choice_player2}')
        print('Player 1 wins')
    elif choice_player1 == 'Stone' and choice_player2 == 'Paper':
        print(f'{choice_player1} against {choice_player2}')
        print('The machine wins')
    elif choice_player1 == 'Stone' and choice_player2 == 'Stone':
        print(f'{choice_player1} against {choice_player2}')
        print('It is a draw!')

def run():
    ## Initialization
    print('Welcome to Scissors, Paper and Stone!')
    choice_player1 = input('What do you choose? Scissors, Paper or Stone? -> ')
    ##Verification process
    if choice_player1 == "Scissors" or choice_player1 == "scissors":
        choice_player1 = choice_player1.capitalize()
        print(f'You have chosen {choice_player1}')
    elif choice_player1 == "Paper" or choice_player1 == "paper":
        choice_player1 = choice_player1.capitalize()
        print(f'You have chosen {choice_player1}')
    elif choice_player1 == "Stone" or choice_player1 == "stone":
        choice_player1 = choice_player1.capitalize() #Capitalize first letter
        print(f'You have chosen {choice_player1}')
    else:
        print('Please, write a valid option')
        run()
    
    ## Player 2 choice ( The machine chooses randomly)
    player2 = choice_player2()
    ## Playing the game
    play(choice_player1, player2)
    

if __name__ == '__main__':
    run()