import board

from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner

# set side based on drive names
name = str(getmount('/').label)
isRight = True if name.endswith('R') else False

# GPIO to key mapping, Left
_KEY_CFG_LEFT = [
    board.GP0, board.GP5, board.GP6,  board.GP9,  board.GP14,
    board.GP1, board.GP4, board.GP7,  board.GP10, board.GP13,
    board.GP2, board.GP3, board.GP8,  board.GP11, board.GP12,
                          board.GP20, board.GP19, board.GP18 
]

# GPIO to key mapping, Left
_KEY_CFG_RIGHT = [
    board.GP14, board.GP9,  board.GP6,  board.GP5, board.GP0,
    board.GP13, board.GP10, board.GP7,  board.GP4, board.GP1,
    board.GP12, board.GP11, board.GP8,  board.GP3, board.GP2,
    board.GP18, board.GP19, board.GP20
]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            pins = _KEY_CFG_RIGHT if isRight == True else _KEY_CFG_LEFT
        )

    # flake8: noqa
    # fmt: off
    coord_mapping = [
         0,  1,  2,  3,  4,   18, 19, 20, 21, 22,
         5,  6,  7,  8,  9,   23, 24, 25, 26, 27,
        10, 11, 12, 13, 14,   28, 29, 30, 31, 32,
                15, 16, 17,   33, 34, 35
    ]
