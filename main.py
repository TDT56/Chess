from var import *


def display_board(board):
    print(board_letters)
    print(board_line)
    for num in num_list[::-1]:
        num = str(num)
        r3 = num + '  |'
        for letter in abc_list:
            # The try and except is only when the actual chess icons is used
            try:
                r2 = f'  {board[letter+num]}   |'
            except KeyError:
                r2 = f'        |'
            r3 = r3 + r2
        print(r3)
        print(board_line)


if __name__ == '__main__':
    display_board(starting_board)