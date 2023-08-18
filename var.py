
# Caps is white and no caps is black
starting_board = {
    'A8': 'r1', 'B8': 'n1', 'C8': 'b1', 'D8': 'q1', 'E8': 'k1', 'F8': 'b2', 'G8': 'n2', 'H8': 'r2',
    'A7': 'p1', 'B7': 'p2', 'C7': 'p3', 'D7': 'p4', 'E7': 'p5', 'F7': 'p6', 'G7': 'p7', 'H7': 'p8',
    'A6': '  ', 'B6': '  ', 'C6': '  ', 'D6': '  ', 'E6': '  ', 'F6': '  ', 'G6': '  ', 'H6': '  ',
    'A5': '  ', 'B5': '  ', 'C5': '  ', 'D5': '  ', 'E5': '  ', 'F5': '  ', 'G5': '  ', 'H5': '  ',
    'A4': '  ', 'B4': '  ', 'C4': '  ', 'D4': '  ', 'E4': '  ', 'F4': '  ', 'G4': '  ', 'H4': '  ',
    'A3': '  ', 'B3': '  ', 'C3': '  ', 'D3': '  ', 'E3': '  ', 'F3': '  ', 'G3': '  ', 'H3': '  ',
    'A2': 'P1', 'B2': 'P2', 'C2': 'P3', 'D2': 'P4', 'E2': 'P5', 'F2': 'P6', 'G2': 'P7', 'H2': 'P9',
    'A1': 'R1', 'B1': 'N1', 'C1': 'B1', 'D1': 'Q1', 'E1': 'K1', 'F1': 'B2', 'G1': 'N2', 'H1': 'R2',
}

testing_board = {
    'A8': 'k1', 'B8': '  ', 'C8': 'k1', 'D8': '  ', 'E8': '  ', 'F8': '  ', 'G8': 'Q1', 'H8': '  ',
    'A7': '  ', 'B7': '  ', 'C7': '  ', 'D7': '  ', 'E7': '  ', 'F7': '  ', 'G7': '  ', 'H7': 'k1',
    'A6': '  ', 'B6': 'k1', 'C6': 'k1', 'D6': 'k1', 'E6': '  ', 'F6': '  ', 'G6': '  ', 'H6': '  ',
    'A5': 'k1', 'B5': 'k1', 'C5': 'k1', 'D5': 'k1', 'E5': '  ', 'F5': '  ', 'G5': '  ', 'H5': '  ',
    'A4': '  ', 'B4': 'k1', 'C4': 'Q1', 'D4': 'k1', 'E4': 'K1', 'F4': '  ', 'G4': '  ', 'H4': 'k1',
    'A3': '  ', 'B3': '  ', 'C3': 'K1', 'D3': '  ', 'E3': '  ', 'F3': '  ', 'G3': '  ', 'H3': '  ',
    'A2': '  ', 'B2': '  ', 'C2': '  ', 'D2': '  ', 'E2': '  ', 'F2': '  ', 'G2': '  ', 'H2': '  ',
    'A1': 'k1', 'B1': '  ', 'C1': '  ', 'D1': 'Q1', 'E1': '  ', 'F1': '  ', 'G1': '  ', 'H1': 'K1',
}

empty_board = {
    'A8': '  ', 'B8': '  ', 'C8': '  ', 'D8': '  ', 'E8': '  ', 'F8': '  ', 'G8': '  ', 'H8': '  ',
    'A7': '  ', 'B7': '  ', 'C7': '  ', 'D7': '  ', 'E7': '  ', 'F7': '  ', 'G7': '  ', 'H7': '  ',
    'A6': '  ', 'B6': '  ', 'C6': '  ', 'D6': '  ', 'E6': '  ', 'F6': '  ', 'G6': '  ', 'H6': '  ',
    'A5': '  ', 'B5': '  ', 'C5': '  ', 'D5': '  ', 'E5': '  ', 'F5': '  ', 'G5': '  ', 'H5': '  ',
    'A4': '  ', 'B4': '  ', 'C4': '  ', 'D4': '  ', 'E4': '  ', 'F4': '  ', 'G4': '  ', 'H4': '  ',
    'A3': '  ', 'B3': '  ', 'C3': '  ', 'D3': '  ', 'E3': '  ', 'F3': '  ', 'G3': '  ', 'H3': '  ',
    'A2': '  ', 'B2': '  ', 'C2': '  ', 'D2': '  ', 'E2': '  ', 'F2': '  ', 'G2': '  ', 'H2': '  ',
    'A1': '  ', 'B1': '  ', 'C1': '  ', 'D1': '  ', 'E1': '  ', 'F1': '  ', 'G1': '  ', 'H1': '  ',
}

# used for software navigate around the board?
num_tup = (1, 2, 3, 4, 5, 6, 7, 8)
abc_tup = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
board_keys = ('A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8',
              'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7',
              'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6',
              'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5',
              'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
              'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
              'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
              'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1')
piece_ids = {'R': 'Rook', 'N': 'Knight', 'B': 'Bishop', 'Q': 'Queen', 'K': 'King', 'P': 'Pawn'}

# same character length as the piece ▭, ―
chess_piece_symbols = {
    'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙',
    'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟',}

board_letters = '       a      b      c      d      e      f      g      h'
board_line = '   ---------------------------------------------------------'

player = ''
