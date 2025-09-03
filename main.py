# Print the board with horizontal lines
# Board with positions 1-9
board = [str(i) for i in range(1, 10)]

win_condition = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7],
                    [2, 4, 6],[2, 5, 8], [3, 4, 5], [6, 7, 8]]


def welcome():
    print('This is a place to play Tic-Tac-Toe.')
    read_rules = input('Do you want to know how to play? Y or N: ')
    if read_rules == 'Y':
        print('Rules:\n'
            'Players: 2 (Player 1 = X, Player 2 = O)\n'
            'Board: 3×3 grid\n\n'
            '🎯 Objective:\n'
            'Be the first to get three of your symbols in a row — either:\n'
            'Horizontally, Vertically or Diagonally.\n\n'
            '🔄 How to Play:\n'
            'Players take turns placing their symbol (X or O) in an empty cell.\n'
            'The game ends when:\n'
            'A player gets 3 in a row → they win, or\n'
            "All 9 cells are filled with no winner → it's a draw')\n")

def print_board(board):
    # Print the board
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")

def check_win(board):
    for condition in win_condition:
        if all(board[i] == current_player for i in condition):
            print_board(board=board)
            print(f'Player {current_player} won the game!')
            exit()
        else:
            continue





welcome()

play_game = input('Would you like to play Tic-Tac_Toe? Answer Y or N :').upper()

if play_game == 'N':
    print('Okay! See you later!')

elif play_game not in ['Y', 'N']:
    print('Invalid input. Boooo. Bye Bye')

elif play_game == 'Y':
    current_player = 'X'
    move_count = 0

    while move_count < 9:
        # show the tic-tac-toe board
        print_board(board=board)

        # counting until all the cells are occupied
        # print(f'move_count is {move_count}')

        # player to place X or O in a chosen cell
        try:
            move = int(input(f'Player {current_player}, can you choose a cell? Choose 1-9 : ')) - 1

        # check if the cell is taken or not
            if board[move] in ['X', 'O']:
                move = int(input((f'The cell {move} is already taken.\n'
                      f'Please choose an empty cell: ')))-1
                board[move] = current_player
            else:
                board[move] = current_player

            # check if the player won or not
            check_win(board=board)

            move_count += 1

            if move_count == 9:
                print_board(board=board)
                print("It's a draw.")
            else:
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'


        except (ValueError, IndexError):
            print("Warning: Invalid input. Please choose a number from 1 - 9.")




