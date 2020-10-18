"""This module has the all the classes needed for the game.
"""

class Board():
    """Main class for the Tic-Tac Toe Board.
    It can generate an arbitrary-sized board,
    handle player moves (place Player instance in board),
    handle game over (win/draw), and generate a nice
    string representation of the board
    """
    def __init__(self, size):
        self.size = size
        self.move_count = 0
        self.game_over = False
        self.board = self.generate_board()

    def __repr__(self):
        """If we call print() on the board
        it will output a nice string (which is
        used during gameplay).
        """
        repr_str = ''
        for i, row in enumerate(self.board):
            # for each even row, we add 3 lines:
            # |- - -|
            # |     |  (repeated n times, n = num_rows)
            # |- - -|  (so then we end up with rows=cols)
            if i % 2 == 0:
                repr_str += '|'
                repr_str += ('').join(['- - -|' for x in row])
                # ('|- - -|- - -|- - -|\n')
                repr_str += '\n'
                repr_str += '|'
                repr_str += ('').join([f'  {x}  |' for x in row])
                repr_str += '\n'
                repr_str += '|'
                repr_str += ('').join(['- - -|' for x in row])
                repr_str += '\n'
            # for each odd row, we only add 1 line:
            # |     |  (repeated n times, n = num_rows)
            else:
                repr_str += '|'
                repr_str += ('').join([f'  {x}  |' for x in row])
                repr_str += '\n'

        if len(self.board) % 2 == 0:
            # if the board has an even number of rows,
            # we need to add a last, closing line:
            # |- - -| * n (repeated n times, n = num_rows)
            repr_str += '|'
            repr_str += ('').join(['- - -|' for x in row])
            repr_str += '\n'

        return repr_str

    def generate_board(self):
        """Creates a 2-d list with
        n elements, where n = board_size
        """

        board = []
        for i in range(self.size):
            board.append([])
            for j in range(self.size):
                board[i].append(' ')
        return board

    def place_move(self, i, j, player):
        """Handles player moves by
        updating the current board
        """
        try:
            if isinstance(self.board[i][j], Player):
                # There is a player instance here already
                return 'Invalid move, try again!'

            self.board[i][j] = player
            self.move_count += 1 # helps to check for draw
            won = self.check_win(i, j, player)

            if isinstance(won, Player):
                # check_win returns a Player object if someone won
                self.game_over = True
                print(self) # 1 print call at the end to display the final board
                return f'THE WINNER IS {str(player)}   !!!\n\n'
            if won == 'draw':
                # If it's a draw it returns 'draw'
                self.game_over = True
                print(self)
                return "It's a draw!"

            # If all went well, we return
            # the board with modified state so we can print it
            return self
        except IndexError:
            # Move out of bounds
            return 'Invalid move, try again!'

    def check_win(self, last_move_x, last_move_y, player):
        """Called after every move to check if someone
        has won or if the game is a draw. It only checks in
        rows and cols where the last move was placed.
        Returns:
        - player if player won
        - 'draw' if it's a draw
        - null otherwise
        """

        # check rows
        for i in range(self.size):
            if self.board[last_move_x][i] != player:
                break
            if i == self.size - 1:
                # Player won
                return player

        # check col
        for i in range(self.size):
            if self.board[i][last_move_y] != player:
                break
            if i == self.size - 1:
                # Player won
                return player

        # check diagonal
        # only if last move was on a diagonal
        if last_move_x == last_move_y:
            for i in range(self.size):
                if self.board[i][i] != player:
                    break
                if i == self.size - 1:
                    # Player won
                    return player

        # check anti diagonal
        # only if last move was on an anti-diagonal
        if last_move_x + last_move_y == self.size - 1:
            for i in range(self.size):
                if self.board[i][(self.size-1) - i] != player:
                    break
                if i == self.size - 1:
                    # Player won
                    return player

        # check draw
        if self.move_count == pow(self.size, 2):
            # If move count = number of squares on the board,
            # then its a draw
            return 'draw'

    def repr_as_simple_string(self):
        """Old, simpler method for __repr__, before
        I came up with the nicer one I use now
        """
        repr_str = '\n'
        for row in self.board:
            if self.size % 3 == 0:
                str_between = '   '
            elif self.size % 2 == 0:
                str_between = '  '
            else:
                str_between = '   '
            repr_str += str_between.join([str(i) for i in row])
            repr_str += '\n\n'
        repr_str += '\n'
        return repr_str

class Player():
    """Simple player class that has a given character (eg. X).
    It returns that character if we call print() on an instance.
    """
    def __init__(self, character):
        self.character = character

    def __repr__(self):
        return self.character

    def __str__(self):
        return self.character

