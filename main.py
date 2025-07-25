# Print the board with horizontal lines
# Board with positions 1-9
board = [str(i) for i in range(1, 10)]

win_condition = [[0, 1, 2], [0, 4, 7], [0, 5, 9],[2, 5, 8],
                    [3, 5, 7],[3, 6, 9], [4, 5, 6], [7, 8, 9]]


def welcome():
    print('This is a place to play Tic-Tac-Toe.')
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
        "All 9 cells are filled with no winner → it's a draw')\n\n")


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
            print('You won the game!')
            exit()
        else:
            continue





welcome()

play_game = input('Would you like to play Tic-Tac_Toe? Answer Y or N :').upper()

if play_game == 'Y':
    current_player = 'X'
    move_count = 0

    while move_count < 9:
        print_board(board=board)
        print(f'move_count is {move_count}')
        try:
            move = int(input(f'Player {current_player}, can you choose a cell? Choose 1-9 : ')) - 1

            if board[move] in ['X', 'O']:
                move = int(input((f'The cell {move} is already taken.\n'
                      f'Please choose an empty cell: ')))
                continue

            board[move] = current_player
            move_count += 1

            check_win(board=board)

            if move_count == 9:
                print("It's a draw.")
                print_board(board=board)
            else:
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'


        except (ValueError, IndexError):
            print("Warning: Invalid input. Please choose a number from 1 - 9.")




