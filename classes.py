

class Board():
    def __init__(self, size):
        self.size = size
        self.board = self.generate_board()

    def __repr__(self):
        repr_str = '\n'
        for row in self.board:
            repr_str += ' '.join([str(i) for i in row])
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
            return self
        except IndexError:
            return 'invalid move'

    def check_win(self, last_move_x, last_move_y, player):

        for i in range(len(self.size)):
            if self.board[last_move_x][i] != player:
                break
            if i == self.size - 1:
                return player

        


class Player():
    def __init__(self, character):
        self.character = character

    def __repr__(self):
        return self.character

    def __str__(self):
        return self.character

