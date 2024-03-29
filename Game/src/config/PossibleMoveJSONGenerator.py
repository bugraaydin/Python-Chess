import json

PossibleMoves = {
    "K": [
        [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1],
        [-3, 0], [2, 0], [3, 0], [-2, 0]  # castle moves
    ]
    ,
    "Q": [
        [-7, 0], [-6, 0], [-5, 0], [-4, 0], [-3, 0], [-2, 0], [-1, 0],
        [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],
        [0, -7], [0, -6], [0, -5], [0, -4], [0, -3], [0, -2], [0, -1],
        [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
        [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7],
        [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7],
        [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7],
        [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]
    ]
    ,
    "R": [
        [-7, 0], [-6, 0], [-5, 0], [-4, 0], [-3, 0], [-2, 0], [-1, 0],
        [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],
        [0, -7], [0, -6], [0, -5], [0, -4], [0, -3], [0, -2], [0, -1],
        [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]
    ]
    ,
    "B": [
        [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7],
        [-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7],
        [1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7],
        [-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7]
    ]
    ,
    "N": [
        [1, 2], [-1, 2],
        [2, 1], [2, -1],
        [1, -2], [-1, -2],
        [-2, 1], [-2, -1]
    ]
    ,
    "P":
        [
            [[0, 1], [-1, 1], [1, 1], [0, 2]],
            [[0, -1], [-1, -1], [1, -1], [0, -2]]
        ]
}


def generate_possible_moves():
    return PossibleMoves
