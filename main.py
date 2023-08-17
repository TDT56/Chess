from var import *
from functions import display_board, selecting_chess_piece
from movement import PieceMovement


if __name__ == '__main__':
    board = testing_board
    player = 'white'
    display_board(board)
    xy = selecting_chess_piece()
    movement = PieceMovement(xy, board)
    movement.movement()
