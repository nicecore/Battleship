class Player:
    """Class of Player objects.
    Players have a name and a list of ships, taken from the Ship class.
    """
    ships = []

    def __init__(self, name):
        self.name = name



class Ship:
    """Ship object containing name, length,
    number of hits, coordinates,
    and whether ship has been sunk.
    """
    
    def __init__(
        self, name, length, 
        hits=0, coordinates=[], 
        sunk=False):

        self.name = name
        self.length = length
        self.hits = hits
        self.coordinates = coordinates
        self.sunk = sunk



class Board:
    """Board object.
    
    self.board -- the list of lists of EMPTYs 
    that is manipulated as players place ships

    self.columns -- the top row of letters on the board

    make_printable() -- renders the list of lists into a viewable board

    """

    def __init__(self):
        self.board = [[EMPTY] * len(range(BOARD_SIZE))
                      for number in range(BOARD_SIZE)]
        self.columns = "    " + \
            " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)])

    def make_printable(self, board):
        myobj = enumerate(self.board, start=1)
        output = []
        for index, value in myobj:
            output.append(' {:<2} {}'.format(index, ' '.join(value)))
        return output

    def __str__(self):
        return self.columns + '\n' + ('\n'.join(self.make_printable(self.board)))



BOARD_SIZE = 10

SHIPS = {
    "a": ("Aircraft Carrier", 5),
    "b": ("Battleship", 4),
    "c": ("Submarine", 3),
    "d": ("Cruiser", 3),
    "e": ("Patrol Boat", 2)
}

COLS = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9
}

TRACKING = {
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    'e': 'e'
}

HIT_TRACKING = {
    'a': 'z',
    'b': 'y',
    'c': 'x',
    'd': 'w',
    'e': 'v'
}

# Similar to SHIPS above, but necessary because computer
# needs to be able to delete items from this one.

ship_choices = {
    'a': 'Aircraft Carrier',
    'b': 'Battleship',
    'c': 'Submarine',
    'd': 'Cruiser',
    'e': 'Patrol Boat'
}

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

COLUMNS = 'abcdefghij'