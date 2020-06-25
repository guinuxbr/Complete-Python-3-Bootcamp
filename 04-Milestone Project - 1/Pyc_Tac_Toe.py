import random

print('Welcome to Tic Tac Toe!')
print('Here goes a filled board for a position reference.\n')
# Displaying the empty board
def display_board(board):
    print(f'{board[7]}|{board[8]}|{board[9]}')
    print('-----')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print('-----')
    print(f'{board[1]}|{board[2]}|{board[3]}\n')

reference_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
display_board(reference_board)

# Making the choice between X and O
def player_input():
    player1 = input("Player 1, please pick a marker 'X' or 'O': ")
    while True:
        if player1.lower() == 'x':
            print('Player 1 mark is X and Player 2 mark is O')
            break
        elif player1.lower() == 'o':
            print('Player 1 mark is O and Player 2 mark is X')
            break
        else:
            player1 = input("Your choice should be only between 'X' or 'O': ")

    if player1.lower() == 'x':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1.upper(), player2.upper())

# Randomly choose the player that will start the game
def choose_first():
    initial_player = random.randint(1, 2)
    if initial_player == 1:
        return "Player 1"
    else:
        return "Player 2"

# Cheking if the place is empty
def space_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False

# Player choice
def player_choice(board):
    player_move = 0
    while player_move not in [1,2,3,4,5,6,7,8,9] or not space_check(board, player_move):
        player_move = int(input('The position should be between 1 and 9: '))

    return player_move

# Make the move
def place_marker(board, marker, position):
    board[position] = marker

# Displaying the board
def win_check(board, mark):
    if (board[7] == board[8] == board[9] == mark) or (board[4] == board[5] == board[6] == mark) or \
        (board[1] == board[2] == board[3] == mark) or (board[1] == board[5] == board[9] == mark) or \
        (board[3] == board[5] == board[7] == mark) or (board[1] == board[4] == board[7] == mark) or \
        (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark):
        print('You win')
        return True
    else:
        return False

# Cheking if the board is full
def full_board_check(board):
    for i in range(1, len(board)):
        if space_check(board, i):
            return False
    return True

# Are want to play again?
def replay():
    play_again = ''
    while play_again != 'Y' or play_again != 'N':
        play_again = input('Do you want to play again? Y or N: ').upper()
        if play_again == 'Y':
            return True
        elif play_again == 'N':
            print('Thank you for playing Pyc Tac Toe!')
            break

# Start to play the game.
while True:
    
    # Setting the board.
    game_board = [' '] * 10

    # Assigning the markers X and Y.
    player1_mark, player2_mark = player_input()

    # Choosing who will play first.
    turn = choose_first()
    print(f'{turn} will begin! Go!')

    play_game = input("Are you ready to play? Y of N: ").upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
        print('Thank you to try Pyc Tac Toe!')
        break

    while game_on:
        if turn == 'Player 1':
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board,player1_mark,position)

            if win_check(game_board,player1_mark):
                display_board(game_board)
                print("Congratulations Player 1. You win!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("Draw game!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board,player2_mark,position)

            if win_check(game_board,player2_mark):
                display_board(game_board)
                print("Congratulations Player 2. You win!")
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("Draw game!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
