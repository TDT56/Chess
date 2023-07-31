def print_hi():
    location_dict = {
        'A8': 0, 'B8': 1, 'C8': 2, 'D8': 3, 'E8': 4, 'F8': 5, 'G8': 6, 'H8': 7,
        'A7': 8, 'B7': 9, 'C7': 10, 'D7': 11, 'E7': 12, 'F7': 13, 'G7': 14, 'H7': 15,
        'A6': 16, 'B6': 17, 'C6': 18, 'D6': 19, 'E6': 20, 'F6': 21, 'G6': 22, 'H6': 23,
        'A5': 24, 'B5': 25, 'C5': 26, 'D5': 27, 'E5': 28, 'F5': 29, 'G5': 30, 'H5': 31,
        'A4': 32, 'B4': 33, 'C4': 34, 'D4': 35, 'E4': 36, 'F4': 37, 'G4': 38, 'H4': 39,
        'A3': 40, 'B3': 41, 'C3': 42, 'D3': 43, 'E3': 44, 'F3': 45, 'G3': 46, 'H3': 47,
        'A2': 48, 'B2': 49, 'C2': 50, 'D2': 51, 'E2': 52, 'F2': 53, 'G2': 54, 'H2': 55,
        'A1': 56, 'B1': 57, 'C1': 58, 'D1': 59, 'E1': 60, 'F1': 61, 'G1': 62, 'H1': 63,
    }

    starting_board = [
        'bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR',
        'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP',
        '',    '',    '',   '',   '',   '',   '',   '',
        '',    '',    '',   '',   '',   '',   '',   '',
        '',    '',    '',   '',   '',   '',   '',   '',
        '',    '',    '',   '',   '',   '',   '',   '',
        'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP',
        'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']

    chess_piece_symbols = {
        'bR': '♖', 'bN': '♘', 'bB': '♗', 'bQ': '♕', 'bK': '♔', 'bP': '♙',
        'wR': '♜', 'wN': '♞', 'wB': '♝', 'wQ': '♛', 'wK': '♚', 'wP': '♟',
    }

    r = ['', '', '', '', '', '', '', '', '']
    board_letters = '       a      b      c      d      e      f      g      h'
    board_line = '    ---------------------------------------------------------'
    board_squares = f'{r[0]} |  {r[1]}  |  {r[2]}  |  {r[3]}  |  {r[4]}  |  {r[5]}  |  {r[6]}  |  {r[7]}  |  {r[8]}  |'

    board = starting_board
    print(board_letters)
    print(board_line)
    for row in range(16):
        if row % 2:
            print(board_line)
        else:
            location = 8 * int(row / 2)
            r3 = ''
            for num, value in enumerate(board[location:location+8]):

                if value == '':
                    value = '  '  # ▭, ―
                r2 = f'  {value}  |'
                if num != 0:
                    r3 = r3 + r2
                else:
                    r1 = f' {int((row/2)+1)}  |'
                    r3 = r1 + r2
            print(r3)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
