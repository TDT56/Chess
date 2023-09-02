from var import *


def selecting_chess_piece(board):
    """
    Constraint should still be added to this function.
    """
    while True:
        xy = input('Enter the coordinates of the piece you would like to select: ')
        xy = xy[0].upper() + xy[1]
        print(f'{xy} - ', end='')
        if valid_selection(xy, board):
            break
    return xy


def display_board(board):
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


def make_lists_equal_length(list1, list2):
    if len(list1) > len(list2):
        difference = len(list1) - len(list2)
        list1 = list1[:-difference]
    elif len(list2) > len(list1):
        difference = len(list2) - len(list1)
        list2 = list2[:-difference]
    return list1, list2
