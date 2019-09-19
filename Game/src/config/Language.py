import enum


# example : c3, h5


class Language(enum):
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    g = 6
    h = 7


"""
K: King
Q: Queen
R: Rook
B: Bishop
N: Knight
P: Pawn (although, by convention, P is usually omitted from notation)
+ check
# checkmate
x captures
0-0 kingside castle
0-0-0 queenside castle
"""