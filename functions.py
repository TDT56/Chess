from var import *


def selecting_chess_piece(board: dict) -> str:
    """
    Allows the user to select a chess piece by entering its coordinates on the board.

    This functions ensures the coordinates is a valid coordinates and capitalizes the letter
    of the coordinates if needed.

    Args:
        board (dict): A dictionary representing the current state of the chessboard.

    Returns:
        str: The selected coordinates (e.g., "A1") of the chess piece.

    """
    while True:
        xy = input('Enter the coordinates of the piece you would like to select: ')
        xy = xy[0].upper() + xy[1]
        print(f'{xy} - ', end='')
        if valid_selection(xy, board):
            break
    return xy


def display_board(board: dict) -> None:
    """
    Display the current chess board.

    Args:
        board (dict): A dictionary representing the current state of the chessboard.

    Display:

         a      b      c      d      e      f      g      h
      -- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --
    8 |  r   |  n   |  b   |  q   |  k   |  b   |  n   |  r   | 8
      -- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --
    7 |  p   |  p   |  p   |  p   |  p   |  p   |  p   |  p   | 7
      -- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --
    6 |      |      |      |      |      |      |      |      | 6
      -- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --
    5 |      |      |      |      |      |      |      |      | 5
      -- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --
    4 |      |      |      |      |      |      |      |      | 4
      -- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --
    3 |      |      |      |      |      |      |      |      | 3
      -- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --
    2 |  P   |  P   |  P   |  P   |  P   |  P   |  P   |  P   | 2
      -- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --
    1 |  R   |  N   |  B   |  Q   |  K   |  B   |  N   |  R   | 1
      -- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --
         a      b      c      d      e      f      g      h

    """
    print(f'\n{board_letters}')
    print(board_line)
    for num in num_tup[::-1]:
        num = str(num)
        r3 = num + ' |'
        for letter in abc_tup:
            # The try and except is only when the actual chess icons is used
            try:
                r2 = f'  {board[letter+num][0]}   |'
            except IndexError:
                r2 = f'      |'
            r3 = r3 + r2
        print(f'{r3} {num}')
        print(board_line)
    print(f'{board_letters}\n')


def valid_selection(xy: str, board: dict) -> bool:
    """
    Validate the user selection.

    Capitalized the xy input and check if it is found in a tuple.
    Return True if found in the tuple otherwise False.

    Args:
        xy (str): Coordinate input from the user
        board (dict): A dictionary representing the current state of the chessboard.

    Return:
        Boolean
    """
    if xy in board_keys:
        if board[xy][0].upper() in piece_ids:
            return True
        else:
            print('You selected an EMPTY space, try again.')
    else:
        print('Invalid Entry!')
    return False


def make_lists_equal_length(list1: list, list2: list) -> (list, list):
    """Trims the longer list to be the same length of shorter one."""
    if len(list1) > len(list2):
        difference = len(list1) - len(list2)
        list1 = list1[:-difference]
    elif len(list2) > len(list1):
        difference = len(list2) - len(list1)
        list2 = list2[:-difference]
    return list1, list2
