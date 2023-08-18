# replacing function should be used for movement
from var import *
from functions import valid_selection, display_board


class PieceMovement:
    def __init__(self, xy, board):
        self.xy = xy
        self.board = board
        self.x = xy[0]
        self.y = str(xy[1])
        self.empty = '  '
        self.movable_coordinates = []

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
                pass
            elif piece_type == 'R':
                print(piece_ids[piece_type])
                self.rook()
            elif piece_type == 'Q':
                print(piece_ids[piece_type])
                pass
            # else King
            else:
                print(piece_ids[piece_type])
                pass
        else:
            print('Movement function unsuccessful validation selection.')
            pass
            # valid_selections already returns a message

    def calculate_direction_movement(self, coordinates):
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
        abc_index = abc_tup.index(self.xy[0])
        num_index = num_tup.index(int(self.xy[1]))
        # Stepping in abc+ direction
        for i, abc in enumerate(abc_tup[abc_index + 1:]):
            coordinates = abc + self.y
            if self.calculate_direction_movement(coordinates):
                break
        # Stepping in abc- direction
        for i, abc in enumerate(reversed(abc_tup[0:abc_index])):
            coordinates = abc + self.y
            if self.calculate_direction_movement(coordinates):
                break
        # Stepping in num+ direction
        for i, num in enumerate(num_tup[num_index + 1:]):
            coordinates = self.x + str(num)
            if self.calculate_direction_movement(coordinates):
                break
        # Stepping in num- direction
        for i, num in enumerate(reversed(num_tup[0:num_index])):
            coordinates = self.x + str(num)
            if self.calculate_direction_movement(coordinates):
                break

        # PRINT MOVABLE COORDINATES
        new_board = empty_board
        for xy_move in self.movable_coordinates:
            new_board[xy_move] = 'X'
        display_board(empty_board)

    def knight(self):
        pass

    def bishop(self):
        pass

    def king(self):
        pass

    def queen(self):
        self.pieces_movement.rook()
        self.pieces_movement.bishop()

    def pawn(self):
        pass


