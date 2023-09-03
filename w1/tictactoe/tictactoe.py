#

import random


X, O = 'X', 'O'
FIELD_SIZE = (3, 3)


def generate_field(rows: int=3, cols: int=3) -> str:
    field = ['_' for x in range(rows*cols)]
    # field[0] = X
    field[2] = X
    # field[3] = X
    field[4] = X
    # field[5] = O
    # field[5] = X
    field[6] = X
    # field[7] = O
    field[8] = X
    return field


def draw_field(field: list, cols: int=3) -> None:
    for row in range(0, len(field), cols):
        print(field[row:row+cols])


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
        if field[row:row+cols].count(O) == cols:
            print(f'{O} has won the game!')


            # print()
            # if field[row:row+cols]:
                # print(field[row:row+cols])
        # if field[3:6]:
        #     print(f'{O} has won the game!')


def main():
    field = generate_field(rows=FIELD_SIZE[0], cols=FIELD_SIZE[1])
    draw_field(field, cols=FIELD_SIZE[1])
    check_winner(field)


if __name__ == '__main__':
    main()
