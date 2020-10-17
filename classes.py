

class Board():
    def __init__(self, size):
        self.size = size
        self.board = self.generate_board()
        self.move_count = 0
        self.game_over = False

    def __repr__(self):
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

    def generate_board(self):

        board = []
        
        for i in range(self.size):
            board.append([])
            for j in range(self.size):
                board[i].append('_')
        return board

    def place_move(self, i, j, player):
        try:
            if isinstance(self.board[i][j], Player):
                return 'invalid move'
            self.board[i][j] = player
            self.move_count += 1
            
            won = self.check_win(i, j, player)
            if isinstance(won, Player):
                self.game_over = True
                print(self)
                return f'{str(player)} won!'
            if won == 'draw':
                self.game_over = True
                print(self)
                return "It's a draw!"
            return self
        except IndexError:
            return 'invalid move'

    def check_win(self, last_move_x, last_move_y, player):

        # check rows
        for i in range(self.size):
            if self.board[last_move_x][i] != player:
                break
            if i == self.size - 1:
                return player

        # check col
        for i in range(self.size):
            if self.board[i][last_move_y] != player:
                break
            if i == self.size - 1:
                return player

        # check diagonal
        if last_move_x == last_move_y:
            for i in range(self.size):
                if self.board[i][i] != player:
                    break
                if i == self.size - 1:
                    return player

        # check anti diagonal
        if last_move_x + last_move_y == self.size - 1:
            for i in range(self.size):
                if self.board[i][(self.size-1) - i] != player:
                    break
                if i == self.size - 1:
                    return player

        # check draw
        if self.move_count == pow(self.size, 2):
            return 'draw'

class Player():
    def __init__(self, character):
        self.character = character

    def __repr__(self):
        return self.character

    def __str__(self):
        return self.character

    def to_str(self):
        return self.character

