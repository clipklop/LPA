#

from enum import Enum
import random


class Mark(Enum):
    CROSS = 'X'
    NOUGHT = 'O'


class Player(Enum):
    HUMAN = 'Human'
    COMP = 'Computer'


# Field size, preferably it should be squared
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


def generate_field(rows: int = 3, cols: int = 3) -> list[str]:
    return ['_' for x in range(rows*cols)]


def draw_field(field: list, cols: int = FIELD_SIZE[1]) -> None:
    for row in range(0, len(field), cols):
        print(field[row:row+cols])
    print('- ' * (len(field)-1))


def get_player() -> str:
    return random.choice((Player.HUMAN.value, Player.COMP.value))


def get_mark() -> str:
    return random.choice((Mark.CROSS.value, Mark.NOUGHT.value))


def player_move(field: list, mark: str) -> list:
    try:
        move = int(input('Enter the position of your move: '))
    except ValueError:
        print("You've to put a valid integer input")
        return player_move(field, mark)
    else:
        while move not in MOVES:
            possible_moves = ' '.join([str(x) for x in MOVES.keys()])
            print(f"Please enter the valid move: {possible_moves}")
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


def check_winner(field: list, player: str, cols: int = FIELD_SIZE[1]) -> str:
    is_active = True
    for i, row in enumerate(range(0, len(field), cols)):
        # Check if X has won
        # By rows
        if field[row:row+cols].count(Mark.CROSS.value) == cols:
            print(f'{player} - {Mark.CROSS.value} has won the game!')
            is_active = False

        # Check if O has won
        # By rows
        if field[row:row+cols].count(Mark.NOUGHT.value) == cols:
            print(f'{player} - {Mark.NOUGHT.value} has won the game!')
            is_active = False

    # Check if X has won
    # By columns
    if field[i::cols].count(Mark.CROSS.value) == cols:
        print(
            f'{player} - {Mark.CROSS.value} has won the game by {i+1} column!'
            )
        is_active = False

    # By diagonal
    if field[::cols+1].count(Mark.CROSS.value) == cols:
        print(f'{player} - {Mark.CROSS.value} has won the game by diagonal!')
        is_active = False

    # By oposite diagonal. Could be buggy for larger grid ;(
    if field[cols-1::cols-1][:-1].count(Mark.CROSS.value) == cols:
        print(
            f'{player} - {Mark.CROSS.value} has won the game by oposite diagonal!'
            )
        is_active = False

    # Check if O has won
    # By columns
    if field[i::cols].count(Mark.NOUGHT.value) == cols:
        print(
            f'{player} - {Mark.NOUGHT.value} has won the game by {i+1} column!'
            )
        is_active = False

    # By diagonal
    if field[::cols+1].count(Mark.NOUGHT.value) == cols:
        print(f'{player} - {Mark.NOUGHT.value} has won the game by diagonal!')
        is_active = False

    # By oposite diagonal. Could be buggy for larger grid ;(
    if field[cols-1::cols-1][:-1].count(Mark.NOUGHT.value) == cols:
        print(
            f'{player} - {Mark.NOUGHT.value} has won the game by oposite diagonal!'
            )
        is_active = False

    # Check for draw
    if field.count('_') == 0:
        print("Wow - it's a draw!")
        is_active = False

    return is_active


def main():
    player, mark = get_player(), get_mark()
    field = generate_field(rows=FIELD_SIZE[0], cols=FIELD_SIZE[1])

    possible_moves = ' '.join([str(x) for x in MOVES.keys()])
    print(f"Enter {possible_moves} to put your mark on the field")

    # Doing our first moves
    if mark == Mark.CROSS.value and player == Player.HUMAN.value:
        last_player = Player.HUMAN.value
        print(f"`{last_player}` is `{Mark.CROSS.value}` so you start first\n")
        player_mark, computer_mark = Mark.CROSS.value, Mark.NOUGHT.value
        draw_field(field)
        p_field = player_move(field, Mark.CROSS.value)
    else:
        last_player = Player.COMP.value
        print(f"`{last_player}` is `{Mark.CROSS.value}` so it starts first\n")
        player_mark, computer_mark = Mark.NOUGHT.value, Mark.CROSS.value
        c_field = comp_move(field, Mark.CROSS.value)
        draw_field(c_field)

    # Iteraiting until we find a winner
    while check_winner(field, last_player):
        if last_player == Player.COMP.value:
            # human move
            p_field = player_move(c_field, player_mark)
            draw_field(p_field)
            last_player = Player.HUMAN.value
        else:
            # comp move
            c_field = comp_move(p_field, computer_mark)
            draw_field(c_field)
            last_player = Player.COMP.value


if __name__ == '__main__':
    main()
