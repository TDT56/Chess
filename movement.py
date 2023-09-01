# replacing function should be used for movement
from var import *
from functions import display_board, make_lists_equal_length


class Movement:
    def __init__(self, xy, board):
        self.xy = xy
        self.board = board
        self.x = xy[0]
        self.y = str(xy[1])
        self.empty = '  '
        self.movable_coordinates = []
        self.abc_index = abc_tup.index(self.xy[0])
        self.num_index = num_tup.index(int(self.xy[1]))

    def available_moves(self):
        """xy: coordinates"""
        piece_type = self.board[self.xy][0].upper()
        print(piece_ids[piece_type])
        if piece_type == 'P':
            self.pawn()
        elif piece_type == 'N':
            self.knight()
        elif piece_type == 'B':
            self.bishop()
        elif piece_type == 'R':
            self.rook()
        elif piece_type == 'Q':
            self.queen()
        elif piece_type == 'K':
            self.king()
        else:
            print('Well this unexpected in the movement function.')

        # PRINT MOVABLE COORDINATES
        new_board = empty_board.copy()
        if len(self.movable_coordinates) != 0:
            for xy_move in self.movable_coordinates:
                new_board[xy_move] = 'X'
            display_board(new_board)
            self.movable_coordinates = []
        else:
            print('No moves available!')

    def calculate_direction_movement(self, coordinates):
        """
        Adds a coordinate to movable coordinates if the cell is empty or occupied by the other player.
        Then returns True if a piece is detected at that coordinate and False when it's empty.

        :param coordinates:
        :return: Boolean
        """
        if self.board[coordinates] == self.empty:
            self.movable_coordinates.append(coordinates)
            return False
        elif (self.board[coordinates][0].isupper() and self.board[self.xy].islower()) or \
                (self.board[coordinates][0].islower() and self.board[self.xy].isupper()):
            self.movable_coordinates.append(coordinates)
            return True
        else:
            return True

    def rook(self):
        # Stepping in abc+ direction and breaks when done
        for abc in abc_tup[self.abc_index + 1:]:
            coordinates = abc + self.y
            if self.calculate_direction_movement(coordinates):
                break
        # Stepping in abc- direction and breaks when done
        for abc in reversed(abc_tup[0:self.abc_index]):
            coordinates = abc + self.y
            if self.calculate_direction_movement(coordinates):
                break
        # Stepping in num+ direction and breaks when done
        for num in num_tup[self.num_index + 1:]:
            coordinates = self.x + str(num)
            if self.calculate_direction_movement(coordinates):
                break
        # Stepping in num- direction and breaks when done
        for num in reversed(num_tup[0:self.num_index]):
            coordinates = self.x + str(num)
            if self.calculate_direction_movement(coordinates):
                break

    def knight(self):
        """
        The knight is written using 8 modified rook movements.
        As an example for one of the modified functions:
        The position of the knight is chosen and an offset on 1 is use from its position.
        Then the modified rook function is used to move 2 position,
        but only the section position is used in this case.
        :return:
        """
        # Stepping in abc+ direction
        if self.x not in ('G', 'H'):
            abc = abc_tup[self.abc_index + 2]
            if self.y != '8':
                coordinates = abc + str(int(self.y) + 1)
                self.calculate_direction_movement(coordinates)
            if self.y != '1':
                coordinates = abc + str(int(self.y)-1)
                self.calculate_direction_movement(coordinates)

        # Stepping in abc- direction
        if self.x not in ('A', 'B'):
            abc = list(reversed(abc_tup[0:self.abc_index-1]))[0]
            if self.y != '8':
                coordinates = abc + str(int(self.y) + 1)
                self.calculate_direction_movement(coordinates)
            if self.y != '1':
                coordinates = abc + str(int(self.y) - 1)
                self.calculate_direction_movement(coordinates)

        # Stepping in num+ direction
        if self.y not in ('7', '8'):
            num = num_tup[self.num_index + 1:][1]
            if self.x != 'A':
                coordinates = chr(ord(self.x) + 1) + str(num)
                self.calculate_direction_movement(coordinates)
            if self.x != 'H':
                coordinates = chr(ord(self.x) - 1) + str(num)
                self.calculate_direction_movement(coordinates)

        # Stepping in num- direction
        if self.y not in ('1', '2'):
            num = list(reversed(num_tup[0:self.num_index-1]))[0]
            if self.x != 'A':
                coordinates = chr(ord(self.x) + 1) + str(num)
                self.calculate_direction_movement(coordinates)
            if self.x != 'H':
                coordinates = chr(ord(self.x) - 1) + str(num)
                self.calculate_direction_movement(coordinates)

    def bishop(self):
        # array of cells in a direction relative to the piece
        abc_plus = abc_tup[self.abc_index + 1:]
        abc_minus = list(reversed(abc_tup[0:self.abc_index]))
        num_plus = num_tup[self.num_index + 1:]
        num_minus = list(reversed(num_tup[0:self.num_index]))

        # Stepping in abc-num+ direction
        _abc_minus, _num_plus = make_lists_equal_length(abc_minus, num_plus)
        for abc, num in zip(abc_minus, num_plus):
            coordinates = abc + str(num)
            if self.calculate_direction_movement(coordinates):
                break

        # Stepping in abc-num- direction
        _abc_minus, _num_minus = make_lists_equal_length(abc_minus, num_minus)
        for abc, num in zip(abc_minus, num_minus):
            coordinates = abc + str(num)
            if self.calculate_direction_movement(coordinates):
                break

        # Stepping in abc+num- direction
        _abc_plus, _num_minus = make_lists_equal_length(abc_plus, num_minus)
        for abc, num in zip(abc_plus, num_minus):
            coordinates = abc + str(num)
            if self.calculate_direction_movement(coordinates):
                break

        # Stepping in abc+num+ direction
        _abc_plus, _num_plus = make_lists_equal_length(abc_plus, num_plus)
        for abc, num in zip(abc_plus, num_plus):
            coordinates = abc + str(num)
            if self.calculate_direction_movement(coordinates):
                break

    def king(self):
        move_abc_minus = self.x != 'A'
        move_num_plus = self.y != '8'
        move_abc_plus = self.x != 'H'
        move_num_minus = self.y != '1'

        if move_abc_minus:
            abc_minus = abc_tup[self.abc_index - 1]
            coordinates = abc_minus + self.y
            self.calculate_direction_movement(coordinates)

        if move_num_plus:
            num_plus = str(num_tup[self.num_index + 1])
            coordinates = self.x + num_plus
            self.calculate_direction_movement(coordinates)

        if move_abc_plus:
            abc_plus = abc_tup[self.abc_index + 1]
            coordinates = abc_plus + self.y
            self.calculate_direction_movement(coordinates)

        if move_num_minus:
            num_minus = str(num_tup[self.num_index - 1])
            coordinates = self.x + num_minus
            self.calculate_direction_movement(coordinates)

        if move_abc_minus and move_num_plus:
            # noinspection PyUnboundLocalVariable
            coordinates = abc_minus + num_plus
            self.calculate_direction_movement(coordinates)
        if move_abc_minus and move_num_minus:
            # noinspection PyUnboundLocalVariable
            coordinates = abc_minus + num_minus
            self.calculate_direction_movement(coordinates)
        if move_abc_plus and move_num_minus:
            # noinspection PyUnboundLocalVariable
            coordinates = abc_plus + num_minus
            self.calculate_direction_movement(coordinates)
        if move_abc_plus and move_num_plus:
            coordinates = abc_plus + num_plus
            self.calculate_direction_movement(coordinates)

    def queen(self):
        self.rook()
        self.bishop()

    def pawn(self):
        move_abc_minus = self.x != 'A'
        move_abc_plus = self.x != 'H'
        if self.board[self.xy][0].isupper():
            is_white = True
        else:
            is_white = False

        if is_white:
            num_plus = str(num_tup[self.num_index + 1])
            coordinates = self.x + num_plus
            if self.board[coordinates] == self.empty:
                self.movable_coordinates.append(coordinates)
                # moving from row 2
                if self.y == '2':
                    coordinates = self.x + '4'
                    # if 2nd open space ahead
                    if self.board[coordinates] == self.empty:
                        self.movable_coordinates.append(coordinates)

            # taking pieces to abc minus side
            if move_abc_minus:
                abc_minus = abc_tup[self.abc_index - 1]
                coordinates = abc_minus + num_plus

                is_black = self.board[coordinates][0].islower()
                if is_black:
                    self.movable_coordinates.append(coordinates)
            # taking pieces to abc plus side
            if move_abc_plus:
                abc_plus = abc_tup[self.abc_index + 1]
                coordinates = abc_plus + num_plus

                is_black = self.board[coordinates][0].islower()
                if is_black:
                    self.movable_coordinates.append(coordinates)

        # if black
        else:
            num_minus = str(num_tup[self.num_index - 1])
            coordinates = self.x + num_minus
            if self.board[coordinates] == self.empty:
                self.movable_coordinates.append(coordinates)
                # moving from row 2
                if self.y == '7':
                    coordinates = self.x + '5'
                    # if 2nd open space ahead
                    if self.board[coordinates] == self.empty:
                        self.movable_coordinates.append(coordinates)

            # taking pieces to abc minus side
            if move_abc_minus:
                abc_minus = abc_tup[self.abc_index - 1]
                coordinates = abc_minus + num_minus

                is_black = self.board[coordinates][0].isupper()
                if is_black:
                    self.movable_coordinates.append(coordinates)
            # taking pieces to abc plus side
            if move_abc_plus:
                abc_plus = abc_tup[self.abc_index + 1]
                coordinates = abc_plus + num_minus

                is_black = self.board[coordinates][0].isupper()
                if is_black:
                    self.movable_coordinates.append(coordinates)

        # REMEMBER THE MOVE WHERE YOU TAKE AN EN PASSANT
