from var import *
from functions import display_board, selecting_chess_piece
from movement import movement


if __name__ == '__main__':
    board = testing_board

    display_board(board)
    xy = selecting_chess_piece()
    movement(xy, board)
