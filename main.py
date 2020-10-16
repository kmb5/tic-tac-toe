from classes import Board, Player

def main():

    board = Board(3)
    player_a = Player('X')
    player_b = Player('O')

    print(board)

    print(board.place_move(0, 0, player_a))
    print(board.place_move(1, 0, player_b))

if __name__ == "__main__":
    main()