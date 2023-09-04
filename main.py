from var import *
from functions import display_board, selecting_chess_piece
from movement import Movement


if __name__ == '__main__':
    print('Start')
    board = starting_board
    player = 'white'
    while True:
        print('INFO: Display Board')
        display_board(board)
        print('INFO: Selecting Chess Pieces')
        xy = selecting_chess_piece(board)
        print('INFO: Movement_01')
        movement = Movement(xy, board)
        print('INFO: Movement_01')
        available_move = movement.available_moves()
        print('INFO: Movement_02')
        if available_move:
            print('INFO: available_move')
            piece = movement.move()
        print('INFO: End of While Loop')


