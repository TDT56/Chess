# replacing function should be used for movement
from var import *
from functions import valid_selection, display_board, make_lists_equal_length


class PieceMovement:
    def __init__(self, xy, board):
        self.xy = xy
        self.board = board
        self.x = xy[0]
        self.y = str(xy[1])
        self.empty = '  '
        self.movable_coordinates = []
        self.abc_index = abc_tup.index(self.xy[0])
        self.num_index = num_tup.index(int(self.xy[1]))

    def movement(self):
        """xy: coordinates"""
        if valid_selection(self.xy, self.board):
            piece_type = self.board[self.xy][0].upper()
            print(piece_ids[piece_type])
            if piece_type == 'P':
                pass
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
        else:
            print('Movement function unsuccessful validation selection.')
            # valid_selections already returns a message

        # PRINT MOVABLE COORDINATES
        new_board = empty_board
        for xy_move in self.movable_coordinates:
            new_board[xy_move] = 'X'
        display_board(new_board)

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

        # Stepping in num+ direction
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
            print(coordinates)
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
        _abc_minus = self.x != abc_tup[0]
        _num_plus = self.y != str(num_tup[-1])
        _abc_plus = self.x != abc_tup[-1]
        _num_minus = self.y != str(num_tup[0])

        if _abc_minus:
            abc_minus = abc_tup[self.abc_index - 1]
            coordinates = abc_minus + self.y
            self.calculate_direction_movement(coordinates)

        if _num_plus:
            num_plus = str(num_tup[self.num_index + 1])
            coordinates = self.x + num_plus
            self.calculate_direction_movement(coordinates)

        if _abc_plus:
            abc_plus = abc_tup[self.abc_index + 1]
            coordinates = abc_plus + self.y
            self.calculate_direction_movement(coordinates)

        if _num_minus:
            num_minus = str(num_tup[self.num_index - 1])
            coordinates = self.x + num_minus
            self.calculate_direction_movement(coordinates)

        if _abc_minus and _num_plus:
            # noinspection PyUnboundLocalVariable
            coordinates = abc_minus + num_plus
            self.calculate_direction_movement(coordinates)
        if _abc_minus and _num_minus:
            # noinspection PyUnboundLocalVariable
            coordinates = abc_minus + num_minus
            self.calculate_direction_movement(coordinates)
        if _abc_plus and _num_minus:
            # noinspection PyUnboundLocalVariable
            coordinates = abc_plus + num_minus
            self.calculate_direction_movement(coordinates)
        if _abc_plus and _num_plus:
            coordinates = abc_plus + num_plus
            self.calculate_direction_movement(coordinates)

    def queen(self):
        self.rook()
        self.bishop()

    def pawn(self):
        pass


