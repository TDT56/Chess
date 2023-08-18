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

            if piece_type == 'P':
                print(piece_ids[piece_type])
                pass
            elif piece_type == 'N':
                print(piece_ids[piece_type])
                pass
            elif piece_type == 'B':
                print(piece_ids[piece_type])
                self.bishop()
                pass
            elif piece_type == 'R':
                print(piece_ids[piece_type])
                self.rook()
            elif piece_type == 'Q':
                print(piece_ids[piece_type])
                self.rook()
                self.bishop()
                pass
            # else King
            else:
                print(piece_ids[piece_type])
                pass
        else:
            print('Movement function unsuccessful validation selection.')
            pass
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
        # Stepping in abc+ direction
        for abc in abc_tup[self.abc_index + 1:]:
            coordinates = abc + self.y
            if self.calculate_direction_movement(coordinates):
                break
        # Stepping in abc- direction
        for abc in reversed(abc_tup[0:self.abc_index]):
            coordinates = abc + self.y
            if self.calculate_direction_movement(coordinates):
                break
        # Stepping in num+ direction
        for num in num_tup[self.num_index + 1:]:
            coordinates = self.x + str(num)
            if self.calculate_direction_movement(coordinates):
                break
        # Stepping in num- direction
        for num in reversed(num_tup[0:self.num_index]):
            coordinates = self.x + str(num)
            if self.calculate_direction_movement(coordinates):
                break

    def knight(self):
        pass

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
        pass

    def queen(self):
        """This function is not required, the rook and bishop functions are used"""
        pass

    def pawn(self):
        pass


