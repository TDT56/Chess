from var import *
from functions import display_board, selecting_chess_piece
from movement import Movement


if __name__ == '__main__':
    board = starting_board
    player = 'white'
    while True:
        display_board(board)
        xy = selecting_chess_piece(board)
        movement = Movement(xy, board)
        movement.available_moves()
