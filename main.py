from classes import Board, Player

def main():

    board_size = select_board_size()
    board = Board(board_size)

    player_characters = select_characters()

    player_a = Player(player_characters[0])
    player_b = Player(player_characters[1])

    previous_player = player_b

    while not board.game_over:
        next_player = player_a if previous_player == player_b else player_b
        round_played = ''

        while round_played in ('', 'invalid move'):
            round_played = play_round(next_player, board)
            print(round_played)
            
        previous_player = next_player


def play_round(player, board):

    print(f'\nPlayer {player} turn.\n')

    move = []

    for i in range(2):
        move_i = ''
        row_or_col = 'row' if i == 0 else 'column'
        while move_i not in [str(x) for x in range(board.size)]:
            move_i = input(f'Select {row_or_col} (1-{board.size}): ')
            try:
                move_i = int(move_i) - 1
                move.append(move_i)
                break
            except (ValueError, IndexError):
                continue

    return board.place_move(move[0], move[1], player)

def select_board_size(): 
    board_size = 0
    while board_size not in range(2,21):
        try:
            board_size = int(input('Select a board size between 2 and 20: '))
        except ValueError:
            continue
    return board_size

def select_characters():

    possible_characters = [
        'X', 'O', '♥️', '✔️', '❌', '💔', '🅾️', '👻', '🎃', '🔥'
    ]

    player_characters = []

    for i in range(1, 3):
        select_string = '\n'.join([f'{str(x + 1)}: {possible_characters[x]}'  for x in range(len(possible_characters))])
        error_msg = f'You must select a number between 1-{len(possible_characters)}: '
        player_select = ''

        while player_select not in [str(x) for x in range(1, len(possible_characters) + 1)]:
            print(select_string)
            player_select = input(f'Player {i} - select your character (type from the numbers above): ')
            try:
                player_select = int(player_select) - 1
                player_character = possible_characters.pop(player_select)
                player_characters.append(player_character)
                print(f'Player {i} - you will play as {player_character}\n')
                break
            except (ValueError, IndexError):
                print(error_msg)
                continue

    return player_characters

    

if __name__ == "__main__":
    main()