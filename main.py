import os
from graphics import board, welcome, add_mark
from rules import (MOVES, BOARD_ARRAY, BOARD_ARRAY_MOVES, TURNS, PLAYERS, PLAYER_NUM,
                   check_winner, find_coordinate)


print(welcome)
print(board)


while True:
    PLAYER_NUM %= len(PLAYERS)  # This variable takes player mark number.
    player = PLAYERS[PLAYER_NUM]  # From list of marks ['X', 'O'] variable takes 'X' or 'O'.

    player_input = find_coordinate(MOVES, player)  # Function checks if coordinate that user give exist
                                                   # in the dictionary of possible coordinations.
    board_place = MOVES[player_input]  # Specific '-' character index number taken from given coordination.

    del MOVES[player_input]  # After user selects coordinate it is deleted from dictionary to avoid repeatability.

    board = add_mark(board, board_place, player)  # Function adds a player mark "X" or "O" into ascii board.

    os.system("cls")
    print(board)  # Shows board after coordinate selection.

    # This part adds X or O mark into array to check possible winner.
    x, y = BOARD_ARRAY_MOVES[player_input]
    BOARD_ARRAY[x][y] = player
    winner = check_winner(BOARD_ARRAY)

    PLAYER_NUM += 1
    TURNS -= 1

    # If winner mark "X" or "O" is given, then it prints the winner.
    if winner:
        print(f"Player {winner} won.")
        break
    # If players run out of moves and winner not found, then program declares a draw.
    if TURNS <= 0:
        print("It is a draw.")
        break






