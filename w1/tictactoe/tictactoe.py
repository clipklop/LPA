#

from typing import Mapping
from enum import Enum
import random


X, O = 'X', 'O'
HUMAN, COMP = 'Human', 'Computer'
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


def generate_field(rows: int=3, cols: int=3) -> list[str]:
    return ['_' for x in range(rows*cols)]


def draw_field(field: list, cols: int=FIELD_SIZE[1]) -> None:
    for row in range(0, len(field), cols):
        print(field[row:row+cols])
    print('- ' * (len(field)-1))


def get_player() -> str:
    return random.choice((HUMAN, COMP))


def get_mark() -> str:
    return random.choice((X, O))


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
        move = MOVES[move]

        if valid_move(field, move):
            field[move] = mark
            return field
        else:
            print('This position is occupied already')
            return player_move(field, mark)


def comp_move(field: list, mark: str) -> list:
    move = random.choice(list(MOVES.keys()))
    move = MOVES[move]

    if valid_move(field, move):
        field[move] = mark
        return field
    else:
        return comp_move(field, mark)


def valid_move(field: list, move: int) -> bool:
    # Check if move would be placed on empty tile
    return field[move] == '_'


def check_winner(field: list, player: str, cols: int=FIELD_SIZE[1]) -> str:
    is_active = True
    for i, row in enumerate(range(0, len(field), cols)):
        # Check if X has won
        # By rows
        if field[row:row+cols].count(X) == cols:
            print(f'{player} - {X} has won the game!')
            is_active = False

        # Check if O has won
        # By rows
        if field[row:row+cols].count(O) == cols:
            print(f'{player} - {O} has won the game!')
            is_active = False

    # Check if X has won
    # By columns
    if field[i::cols].count(X) == cols:
        print(f'{player} - {X} has won the game by {i+1} column!')
        is_active = False
    
    # By diagonal
    if field[::cols+1].count(X) == cols:
        print(f'{player} - {X} has won the game by diagonal!')
        is_active = False

    # By oposite diagonal. Could be buggy for larger grid ;(
    if field[cols-1::cols-1][:-1].count(X) == cols:
        print(f'{player} - {X} has won the game by oposite diagonal!')
        is_active = False

    # Check if O has won
    # By columns
    if field[i::cols].count(O) == cols:
        print(f'{player} - {O} has won the game by {i+1} column!')
        is_active = False
    
    # By diagonal
    if field[::cols+1].count(O) == cols:
        print(f'{player} - {O} has won the game by diagonal!')
        is_active = False

    # By oposite diagonal. Could be buggy for larger grid ;(
    if field[cols-1::cols-1][:-1].count(O) == cols:
        print(f'{player} - {O} has won the game by oposite diagonal!')
        is_active = False
    
    # Check for draw
    if field.count('_') == 0:
        print(f"Wow - it's a draw!")
        is_active = False

    return is_active


def main():
    player, mark = get_player(), get_mark()
    field = generate_field(rows=FIELD_SIZE[0], cols=FIELD_SIZE[1])
    
    possible_moves = ' '.join([str(x) for x in MOVES.keys()])
    print(f"Enter {possible_moves} to put your mark on the field")
    
    # Doing our first moves
    if mark == X and player == HUMAN:
        last_player = HUMAN
        print(f"`{last_player}` is `{X}` so you start first\n")
        player_mark, computer_mark = X, O
        draw_field(field)
        p_field = player_move(field, X)
    else:
        last_player = COMP
        print(f"`{last_player}` is `{X}` so it starts first\n")
        player_mark, computer_mark = O, X
        c_field = comp_move(field, X)
        draw_field(c_field)

    # Iteraiting until we find a winner
    while check_winner(field, last_player):
        if last_player == COMP:
            # human move
            p_field = player_move(c_field, player_mark)
            draw_field(p_field)
            last_player = HUMAN
        else:
            # comp move
            c_field = comp_move(p_field, computer_mark)
            draw_field(c_field)
            last_player = COMP


if __name__ == '__main__':
    main()
