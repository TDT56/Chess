# replacing function should be used for movement
from var import *
from functions import valid_selection


class PieceMovement:
    def __init__(self, xy, board):
        self.xy = xy
        self.board = board
        self.x = xy[0]
        self.y = str(xy[1])
        self.empty = ' '
        self.movable_coordinates = []

    def movement(self):
        """xy: coordinates"""
        print('Execute movement function') if comments else None
        if valid_selection(self.xy, self.board):
            piece_type = self.board[self.xy][0].upper()

            if piece_type == 'P':
                print('P')
                pass
            elif piece_type == 'N':
                print('N')
                pass
            elif piece_type == 'B':
                print('P')
                pass
            elif piece_type == 'R':
                print('R')
                self.rook()
            elif piece_type == 'Q':
                print('Q')
                pass
            # else King
            else:
                print('K')
                pass
        else:
            print('Movement function unsuccessful validation selection.')
            pass
            # valid_selections already returns a message

    def calculate_direction_movement(self, coordinates):
        if self.board[coordinates] == self.empty:
            self.movable_coordinates.append(coordinates)
            return False
        elif (self.board[coordinates][0].isupper() and self.x.islower()) or \
                (self.board[coordinates][0].islower() and self.x.isupper()):
            self.movable_coordinates.append(coordinates)
            return False
        else:
            return True

    def rook(self):

        movable_coordinates = []
        print('Entered the rook')
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

        print(self.movable_coordinates)

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


