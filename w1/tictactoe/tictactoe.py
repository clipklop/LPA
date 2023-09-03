#

import random



X, O = 'X', 'O'
HUMAN, COMP = 'human', 'comp'
FIELD_SIZE = (3, 3)

# Possible moves
MOVES = {
    11: 0,
    12: 1,
    13: 2,
    21: 3,
    22: 4,
    23: 5,
    31: 6,
    32: 7,
    33: 8,
}


def generate_field(rows: int=3, cols: int=3) -> str:
    field = ['_' for x in range(rows*cols)]
    # # field[0] = X
    # field[2] = X
    # # field[3] = X
    # field[4] = X
    # # field[5] = O
    # # field[5] = X
    # field[6] = X
    # # field[7] = O
    # field[8] = X
    return field


def draw_field(field: list, cols: int=FIELD_SIZE[1]) -> None:
    for row in range(0, len(field), cols):
        print(field[row:row+cols])
    print('- ' * (len(field)-1))


def get_player() -> dict:
    return {
        'player': random.choice((HUMAN, COMP)),
        'mark': random.choice((X, O))
    }


def game_start(player: str, mark: str):
    if mark == X and player == 'human':
        print('OMG!')
        return 
# def move_field(field: list, move: int, player: str) -> list:
#     # new_field = field[:]
#     field[MOVES[move]] = player
    
#     return field


def player_move(field: list, mark: str) -> list:
    try:
        move = int(input('Enter the position of your move: '))
    except ValueError:
        print(f"You've to put a valid integer input")
        return player_move(field, mark)
    else:
        while move not in MOVES:
            print(f"Please enter the valid move: {' '.join([str(x) for x in MOVES.keys()])}")
            return player_move(field, mark)
        
        # Make move on the field
        field[MOVES[move]] = mark
        return field


def comp_move(field: list, mark: str) -> list:
    move = random.choice(list(MOVES.keys()))
    print(move)
    field[MOVES[move]] = mark
    return field


def check_winner(field: list, cols: int=3) -> str:
    for i, row in enumerate(range(0, len(field), cols)):
        # Check if X has won
        # By rows
        if field[row:row+cols].count(X) == cols:
            print(f'{X} has won the game!')          

        # By columns
        if field[i::cols].count(X) == cols:
            print(f'{X} has won the game by {i+1} column!')
        
        # By diagonal
        if field[::cols+1].count(X) == cols:
            print(f'{X} has won the game by diagonal!')

        # By oposite diagonal. Could be buggy for larger grid ;(
        if field[cols-1::cols-1][:-1].count(X) == cols:
            print(f'{X} has won the game by oposite diagonal!')
            break

        # Check if O has won
        # By rows
        if field[row:row+cols].count(O) == cols:
            print(f'{O} has won the game!')

        # By columns
        if field[i::cols].count(O) == cols:
            print(f'{O} has won the game by {i+1} column!')
        
        # By diagonal
        if field[::cols+1].count(O) == cols:
            print(f'{O} has won the game by diagonal!')

        # By oposite diagonal. Could be buggy for larger grid ;(
        if field[cols-1::cols-1][:-1].count(O) == cols:
            print(f'{O} has won the game by oposite diagonal!')
            break


def main():
    field = generate_field(rows=FIELD_SIZE[0], cols=FIELD_SIZE[1])
    # check_winner(field)
    
    player = get_player()['player']
    mark = get_player()['mark']
    print(player, mark)

    if mark == X and player == HUMAN:
        last_player = HUMAN
        p_mark, c_mark = X, O
        draw_field(field)
        p_field = player_move(field, X)
    else:
        last_player = COMP
        p_mark, c_mark = O, X
        c_field = comp_move(field, X)
        draw_field(c_field)

    while True:
        if last_player == COMP:
            # human move
            p_field = player_move(c_field, p_mark)
            draw_field(p_field)
            last_player = HUMAN
        else:
            # comp move
            c_field = comp_move(p_field, c_mark)
            draw_field(c_field)
            last_player = COMP


if __name__ == '__main__':
    main()
