from functions import *
from movement import Movement


if __name__ == '__main__':
    print('Start')
    board = starting_board

    update_position_list(board=board, section='initialize')
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
            moved_piece, piece_taken, new_xy = movement.move()
            update_position_list(moved_piece=moved_piece, new_coordinates=new_xy, piece_taken=piece_taken)

        print('INFO: End of While Loop')


