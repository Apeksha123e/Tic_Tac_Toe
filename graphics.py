welcome ="""
 __      __       .__                                  __               
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____       
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \      
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )     
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/      
       \/       \/          \/            \/     \/                     
___________.__         ___________               ___________            
\__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____  
  |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \ 
  |    |   |  \  \___    |    |   / __ \\  \___    |    |(  <_> )  ___/ 
  |____|   |__|\___  >   |____|  (____  /\___  >   |____| \____/ \___  >
                   \/                 \/     \/                      \/ 
Welcome to Tic Tac Toe Game. To choose coordinates use board references.\n
For example, if you want to put X on the top-left corner, write '1a'. \n
Good Luck!
"""

board = """
     A  |  B  |  C
   ------------------
  |     |     |      |
1 |  -  |  -  |  -   |
__|_____|_____|_____ |
  |     |     |      |
2 |  -  |  -  |  -   |
__|_____|_____|_____ |
  |     |     |      |
3 |  -  |  -  |  -   |
  |     |     |      |
   ------------------      
"""


def add_mark(board_ascii: str, char_index: int, mark: str) -> str:
    """
    Function adds mark (X or O) into ascii str board.
    :param board_ascii: string of ascii board.
    :param char_index: integer value of index where mark should be replaced in the board.
    :param mark: string of mark (X or O)
    :return: returns updated board with new mark added.
    """
    list_board = list(board_ascii)
    list_board[char_index] = mark
    board_updated = "".join(list_board)
    return board_updated

