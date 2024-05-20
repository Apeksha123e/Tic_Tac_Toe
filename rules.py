import numpy
import numpy as np

TURNS = 9  # Possible moves in the 3x3 Tic Tac Toe game
PLAYERS = ["X", "O"]  # Players marks
PLAYER_NUM = 0  # First player that starts the game

MOVES = {
    "1a": 70, "1b": 76, "1c": 82,
    "2a": 139, "2b": 145, "2c": 151,
    "3a": 208, "3b": 214, "3c": 220
}  # Keys as coordinates in the board and values as '-' char indexes of ascii board.

BOARD_ARRAY = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]  # Array of empty board where X's and O's will be given.

BOARD_ARRAY_MOVES = {
    "1a": [0, 0], "1b": [0, 1], "1c": [0, 2],
    "2a": [1, 0], "2b": [1, 1], "2c": [1, 2],
    "3a": [2, 0], "3b": [2, 1], "3c": [2, 2]
}  # Keys as coordinates in the ascii board and values as indexes of an array board.


def check_winner(array_: numpy.ndarray):
    """
    Function checks array to find the winner of tic-tac-toe game. First it checks rows as if there
    a set that only contains one value of "X" or "O". Also, it checks columns and diagonal rows.
    :param array_: numpy.ndarray 3x3 shape with "X", "O" and numbers (default empty value for tic-tac-toe game).
    :return: If column, row or diagonal row consists of only one value, for example, only "O". It returns
    that particular value, otherwise it returns False.
    """
    for row in array_:
        if len(set(row)) == 1:
            return row[0]
    for column in np.transpose(array_):
        if len(set(column)) == 1:
            return column[0]
    if len(set([array_[i][i] for i in range(len(array_))])) == 1:
        return array_[0][0]
    if len(set([array_[i][len(array_) - i - 1] for i in range(len(array_))])) == 1:
        return array_[0][len(array_) - 1]
    return False


def find_coordinate(coordinate_keys: dict, player_mark: str) -> str:
    """
    Function checks if the coordinate that users gives exist in the dictionary of
    coordinates. Otherwise, it would not let the program crash if the user gives wrong
    coordinates multiple times.
    :param coordinate_keys: dictionary of coordinates, for example: {"1a": 293, "1b": 333, etc.}
    :param player_mark: Mark of the player - "X" or "O"
    :return: When user given coordinate found in the dict, it returns user input.
    """
    while True:
        user_input = input(f"Player ({player_mark}) choose coordination: ").lower().strip()
        if user_input in coordinate_keys.keys():
            return user_input
        else:
            print("Wrong coordinate or place already taken. Please try again.")
