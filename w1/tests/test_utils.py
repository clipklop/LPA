#

from tictactoe.tictactoe import FIELD_SIZE, generate_field, valid_move


field = generate_field(rows=FIELD_SIZE[0], cols=FIELD_SIZE[1])


def test_field_size_is_valid():
    assert len(field) == FIELD_SIZE[0]*FIELD_SIZE[1]


def test_is_valid_move():
    assert valid_move(field, 1) == True
