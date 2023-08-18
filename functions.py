from var import *


def selecting_chess_piece():
    """
    Constraint should still be added to this function.
    """
    x = input('Enter the coordinates of the piece you would like to select: ')
    x = x[0].upper() + x[1]
    print(f'{x} - ', end='')
    return x


def display_board(board):
    print(board_letters)
    print(board_line)
    for num in num_tup[::-1]:
        num = str(num)
        r3 = num + '  |'
        for letter in abc_tup:
            # The try and except is only when the actual chess icons is used
            try:
                r2 = f'  {board[letter+num][0]}   |'
            except IndexError:
                r2 = f'      |'
            r3 = r3 + r2
        print(r3)
        print(board_line)


def valid_selection(xy: str, board: dict):
    """Validate the user selection"""
    if xy in board_keys:
        if board[xy][0].upper() in piece_ids:
            return True
        else:
            print('You selected an EMPTY space, try again.')
    else:
        print('Invalid Entry!')
    return False
