# replacing function should be used for movement
from var import *
from functions import valid_selection


def movement(xy, board):
    """xy: coordinates"""
    print('Execute movement function') if comments else None
    if valid_selection(xy, board):
        piece_id = board[xy]
        piece_type = board[xy][0].upper()

        if piece_type == 'P':
            print('P')
            pass
        elif piece_type == 'N':
            print('N')
            pass
        elif piece_type == 'B':
            print('P')
            pass
        elif piece_type == 'R':
            print('R')
            rook(xy, board)
        elif piece_type == 'Q':
            print('Q')
            pass
        # else King
        else:
            print('K')
            pass
    else:
        print('Movement function unsuccessful validation selection.')
        pass
        # valid_selections already returns a message


def rook(xy, board):
    movable_coordinates = []
    empty = ' '
    x = xy[0]
    y = str(xy[1])
    print('Entered the rook')
    abc_index = abc_tup.index(xy[0])
    num_index = num_tup.index(int(xy[1]))

    # Stepping in abc+ direction
    for i, abc in enumerate(abc_tup[abc_index + 1:]):
        coordinates = abc + y
        if board[coordinates] == empty:
            movable_coordinates.append(coordinates)
        else:
            movable_coordinates.append(coordinates)
            break

    a1 = len(movable_coordinates)
    print(f'{a1} right')

    # Stepping in abc- direction
    for i, abc in enumerate(reversed(abc_tup[0:abc_index])):
        coordinates = abc + y
        if board[coordinates] == empty:
            movable_coordinates.append(coordinates)
        else:
            movable_coordinates.append(coordinates)
            break

    a2 = len(movable_coordinates)
    print(f'{a2-a1} left')

    # Stepping in num+ direction
    for i, num in enumerate(num_tup[num_index + 1:]):
        coordinates = x + str(num)
        if board[coordinates] == empty:
            movable_coordinates.append(coordinates)
        else:
            movable_coordinates.append(coordinates)
            break

    a3 = len(movable_coordinates)
    print(f'{a3-a2} up')

    # Stepping in num- direction
    for i, num in enumerate(reversed(num_tup[0:num_index])):
        coordinates = x + str(num)
        if board[coordinates] == empty:
            movable_coordinates.append(coordinates)
        else:
            movable_coordinates.append(coordinates)
            break

    a4 = len(movable_coordinates)
    print(f'{a4-a3} down')

    print(movable_coordinates)


def knight():
    pass


def bishop():
    pass


def king():
    pass


def queen():
    rook()
    bishop()


def pawn():
    pass


