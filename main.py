from var import *


def display_board():
    # this is for a list, a dictionary will be used
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


if __name__ == '__main__':
    print_hi()