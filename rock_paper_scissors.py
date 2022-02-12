import random

game = {
    'r':'Rock',
    'p':'Paper',
    's':'Scissors'
}

username = input('Enter your name:')

round = int(input('How many rounds do you play: '))

user_score = 0
ai_score = 0


while True:
    print(f'\n{username} score: {user_score}\tComputer score: {ai_score}')
    user_choice = input('\nChoose between Rock, Paper and Scissors (enter r,p or s):')
    ai_choice = random.choice(list(game.keys()))
    print(f'Your choice: {game[user_choice]}\nComputer choice: {game[ai_choice]}')

    if (user_choice == 'r' and ai_choice == 's') or (user_choice == 's' and ai_choice == 'p') or (user_choice == 'p' and ai_choice == 'r'):
        print('You won!')
        user_score += 1
    elif user_choice != ai_choice:
        print('You lost!')
        ai_score += 1
    else:
        print('Draw!')

    if user_score == round // 2 + 1 and ai_score != user_score:
        print(f'\n************* You won the game {user_score} - {ai_score} *************')
        break
    elif ai_score == round // 2 + 1 and ai_score != user_score:
        print(f'\n************* You lost the game {user_score} - {ai_score} *************')
        break
    elif ai_score == round // 2 and user_score == round // 2:
        print('\n************* Draw *************')
        break