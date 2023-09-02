# replacing function should be used for movement
from var import *
from functions import display_board, make_lists_equal_length


class Movement:
    def __init__(self, xy, board):
        """
        Initialize a ChessPiece object.

        :param str xy: The coordinates of the chess piece (e.g., "A1").
        :param dict board: A dictionary representing the current state of the chessboard.

        This constructor initializes a ChessPiece object with the given coordinates and
        sets various attributes to manage the piece's state.

        :var str xy: The coordinates of the chess piece.
        :var dict board: The current state of the chessboard.
        :var str x: The x-coordinate (column) of the chess piece.
        :var str y: The y-coordinate (row) of the chess piece.
        :var str empty: The representation of an empty square on the chessboard.
        :var list movable_coordinates: A list of valid destination coordinates based on game rules.
        :var int abc_index: The index of the x-coordinate (column) in the "abc_tup" tuple.
        :var int num_index: The index of the y-coordinate (row) in the "num_tup" tuple.
        """
        self.xy = xy
        self.board = board
        self.x = xy[0]
        self.y = str(xy[1])
        self.empty = '  '
        self.movable_coordinates = []
        self.abc_index = abc_tup.index(self.xy[0])
        self.num_index = num_tup.index(int(self.xy[1]))

    def move(self) -> None:
        """
        Move a chess piece on the board to a valid destination.

        This method allows a player to move a chess piece to a new location on the chessboard.
        It prompts the player to enter the coordinates (e.g., "A1", "B2") of the destination
        square where they want to move their piece. The method ensures that the entered
        coordinates are valid and represent a legal move according to the current game rules.

        If the entered coordinates are valid, the method replaces the piece at the
        current square with an empty square and replaces the destination square with
        the current piece.

        Note:
            - The `movable_coordinates` attribute should contain the list of valid
              destination coordinates based on the rules of the game.
            - The `board` attribute represents the current state of the chessboard.
            - The `empty` attribute represents an empty square on the board.

        Returns:
            None
        """
        while True:
            xy = input('Enter the coordinates where you want to move you piece to: ')
            xy = xy[0].upper() + xy[1]
            if xy in self.movable_coordinates:
                break
            else:
                print('Wrong entry, try again.')
        self.board[self.xy], self.board[xy] = self.empty, self.board[self.xy]

    def available_moves(self):
        """
        Determine and print the available moves for a chess piece.

        This function calculates and prints the available moves for the chess piece
        represented by the current object. It identifies the piece type based on the
        chessboard's current state and then calls the corresponding piece-specific
        method (e.g., pawn(), knight(), etc.) to calculate the valid moves.
        """
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
        self.print_movable_coordinates()

    def print_movable_coordinates(self):
        """Print the movable coordinates on the chessboard."""
        new_board = empty_board.copy()
        if len(self.movable_coordinates) != 0:
            for xy_move in self.movable_coordinates:
                new_board[xy_move] = 'X'
            display_board(new_board)
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
        """Calculate valid moves for a Rook."""

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
        """Calculate valid moves for a Knight."""
        # Jumping in abc+ direction
        if self.x not in ('G', 'H'):
            # Take two steps to the abc+ direction
            abc = abc_tup[self.abc_index + 2]
            if self.y != '8':
                # Take a step to the str+ direction
                coordinates = abc + str(int(self.y) + 1)
                self.calculate_direction_movement(coordinates)
            if self.y != '1':
                # Take a step to the str- direction
                coordinates = abc + str(int(self.y) - 1)
                self.calculate_direction_movement(coordinates)

        # Jumping in abc- direction
        if self.x not in ('A', 'B'):
            # Take two steps to the abc- direction
            abc = list(reversed(abc_tup[0:self.abc_index-1]))[0]
            if self.y != '8':
                # Take a step to the str+ direction
                coordinates = abc + str(int(self.y) + 1)
                self.calculate_direction_movement(coordinates)
            if self.y != '1':
                # Take a step to the str- direction
                coordinates = abc + str(int(self.y) - 1)
                self.calculate_direction_movement(coordinates)

        # Jumping in num+ direction
        if self.y not in ('7', '8'):
            # Take two steps to the num+ direction
            num = num_tup[self.num_index + 1:][1]
            if self.x != 'A':
                # Take a step to the abc+ direction
                coordinates = chr(ord(self.x) + 1) + str(num)
                self.calculate_direction_movement(coordinates)
            if self.x != 'H':
                # Take a step to the abc- direction
                coordinates = chr(ord(self.x) - 1) + str(num)
                self.calculate_direction_movement(coordinates)

        # Jumping in num- direction
        if self.y not in ('1', '2'):
            # Take two steps to the num- direction
            num = list(reversed(num_tup[0:self.num_index-1]))[0]
            if self.x != 'A':
                # Take a step to the abc+ direction
                coordinates = chr(ord(self.x) + 1) + str(num)
                self.calculate_direction_movement(coordinates)
            if self.x != 'H':
                # Take a step to the abc- direction
                coordinates = chr(ord(self.x) - 1) + str(num)
                self.calculate_direction_movement(coordinates)

    def bishop(self):
        """Calculate valid moves for a Bishop."""
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
        """Calculate valid moves for a King."""
        move_abc_minus = self.x != 'A'
        move_num_plus = self.y != '8'
        move_abc_plus = self.x != 'H'
        move_num_minus = self.y != '1'

        # abc- direction
        if move_abc_minus:
            abc_minus = abc_tup[self.abc_index - 1]
            coordinates = abc_minus + self.y
            self.calculate_direction_movement(coordinates)

        # num+ direction
        if move_num_plus:
            num_plus = str(num_tup[self.num_index + 1])
            coordinates = self.x + num_plus
            self.calculate_direction_movement(coordinates)

        # abc+ direction
        if move_abc_plus:
            abc_plus = abc_tup[self.abc_index + 1]
            coordinates = abc_plus + self.y
            self.calculate_direction_movement(coordinates)

        # num- direction
        if move_num_minus:
            num_minus = str(num_tup[self.num_index - 1])
            coordinates = self.x + num_minus
            self.calculate_direction_movement(coordinates)

        # abc-num+ direction
        if move_abc_minus and move_num_plus:
            # noinspection PyUnboundLocalVariable
            coordinates = abc_minus + num_plus
            self.calculate_direction_movement(coordinates)

        # abc-num- direction
        if move_abc_minus and move_num_minus:
            # noinspection PyUnboundLocalVariable
            coordinates = abc_minus + num_minus
            self.calculate_direction_movement(coordinates)

        # abc+num- direction
        if move_abc_plus and move_num_minus:
            # noinspection PyUnboundLocalVariable
            coordinates = abc_plus + num_minus
            self.calculate_direction_movement(coordinates)

        # abc+num+ direction
        if move_abc_plus and move_num_plus:
            coordinates = abc_plus + num_plus
            self.calculate_direction_movement(coordinates)

    def queen(self):
        """Calculate valid moves for a Queen."""
        self.rook()
        self.bishop()

    def pawn(self):
        """Calculate valid moves for a Pawn."""
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

            # taking pieces to abc- side
            if move_abc_minus:
                abc_minus = abc_tup[self.abc_index - 1]
                coordinates = abc_minus + num_plus

                is_black = self.board[coordinates][0].islower()
                if is_black:
                    self.movable_coordinates.append(coordinates)
            # taking pieces to abc+ side
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

            # taking pieces to abc- side
            if move_abc_minus:
                abc_minus = abc_tup[self.abc_index - 1]
                coordinates = abc_minus + num_minus

                is_black = self.board[coordinates][0].isupper()
                if is_black:
                    self.movable_coordinates.append(coordinates)
            # taking pieces to abc+ side
            if move_abc_plus:
                abc_plus = abc_tup[self.abc_index + 1]
                coordinates = abc_plus + num_minus

                is_white = self.board[coordinates][0].isupper()
                if is_white:
                    self.movable_coordinates.append(coordinates)

        # REMEMBER THE MOVE WHERE YOU TAKE AN EN PASSANT
