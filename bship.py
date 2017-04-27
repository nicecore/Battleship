import os

##########################################################################

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
    
##########################################################################

# Clear screen function


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


##########################################################################

def choice_getter(board, player):
    ships_to_choose = [
        ['a', 'Aircraft Carrier'],
        ['b', 'Battleship'],
        ['c', 'Submarine'],
        ['d', 'Cruiser'],
        ['e', 'Patrol Boat']
    ]

    while ships_to_choose:
        clear_screen()
        print(board)
        print("\n{}, which ship would you like to place?\n".format(player.name))
        for i, j in ships_to_choose:
            print("[{}] {}".format(i, j))
        user_choice = input("\n> ").lower()
        if user_choice in ship_choices.keys():
            for i in ships_to_choose:
                if i[0] == user_choice:
                    ships_to_choose.remove(i)
            ship_placer(board, user_choice, player)

        else:
            input("\nSorry, that's not a valid choice. Hit ENTER to continue...")


##########################################################################

def ship_placer(board, choice, player):
    clear_screen()
    unplaced=True
    while unplaced:
        clear_screen()
        print(board)
        horiz_vert = input("""
{}, would you like to place your {} horizontally or vertically? Remember that the
{} takes up {} spaces! Ships will be placed from left to right and from top to bottom.
Please type 'H' for horizontal and 'V' for vertical and press ENTER.\n 
>""".format(player.name, SHIPS[choice][0], SHIPS[choice][0], SHIPS[choice][1])).lower()
        if horiz_vert == 'h':
            clear_screen()
            print(board)
            col_choice = input("\nPlease specify a column:\n> ").lower()
            clear_screen()
            print(board)
            row_choice = input("\nPlease specify a row:\n> ")
            try:
                row_choice = int(row_choice)
            except ValueError:
                row_choice = 99
            if row_choice in list(range(1, 11)) and col_choice in COLS.keys():
                if len(board.board[row_choice - 1][COLUMNS.index(col_choice):]) >= SHIPS[choice][1] and all(p == EMPTY for p in (board.board[row_choice - 1][COLS[col_choice]:(COLS[col_choice] + SHIPS[choice][1])])) == True:
                    col = COLUMNS.index(col_choice)
                    row = row_choice - 1
                    player.ships[choice].coordinates = [(row, col)]
                    for i in range(player.ships[choice].length - 1):
                        col += 1
                        player.ships[choice].coordinates.append((row, col))
                    for i, j in player.ships[choice].coordinates:
                        board.board[i][j] = HORIZONTAL_SHIP
                    unplaced = False
                else:
                    input("Sorry, your ship goes off the map or intersects with a previously placed ship. Press ENTER to try again...")

            else:
                clear_screen()
                print(board)
                input(
                    "\nSorry, your column or row choice was invalid. Please press ENTER to try again...")
        if horiz_vert == 'v':
            clear_screen()
            print(board)
            col_choice = input("\nPlease specify a column:\n> ").lower()
            clear_screen()
            print(board)
            row_choice = input("\nPlease specify a row:\n> ")
            try:
                row_choice = int(row_choice)
            except ValueError:
                row_choice = 99
            if row_choice in list(range(1, 11)) and col_choice in COLS.keys():
                if player.ships[choice].length <= len(board.board[row_choice - 1:]):
                    holder = []
                    for i in board.board[row_choice - 1:SHIPS[choice][1]]:
                        holder.append(i[COLUMNS.index(col_choice)])
                    if all(p == EMPTY for p in holder):
                        col = COLUMNS.index(col_choice)
                        row = row_choice - 1
                        player.ships[choice].coordinates = [(row, col)]
                        for i in range(player.ships[choice].length - 1):
                            row += 1
                            player.ships[choice].coordinates.append((row, col))
                        for i, j in player.ships[choice].coordinates:
                            board.board[i][j] = VERTICAL_SHIP
                        unplaced = False
                    else:
                        clear_screen()
                        print(board)
                        input("\nSorry, the ship cannot intersect with a previously placed ship. Press ENTER to try again...")

                else:
                    clear_screen()
                    print(board)
                    input("\nSorry, your ship cannot be placed off of the map. Please press ENTER to try again...")

            else:
                clear_screen()
                print(board)
                input(
                    "\nSorry, your column or row choice was invalid. Please press ENTER to try again...") 

##########################################################################

def turn_taker(attacker, defender, attacker_main, defender_main, defender_view):
    shooting = True
    clear_screen()
    input("\nIt's {}'s turn! Please press ENTER when {} has the computer.".format(attacker.name, attacker.name))
    while shooting:
        clear_screen()
        print("    {}'s Board\n".format(defender.name))
        print(defender_view)
        print('\n')
        print("    {}'s Board\n".format(attacker.name))
        print(attacker_main)
        col_choice = input("\nTake your best shot, {}! Please choose a column:\n> ".format(attacker.name)).lower()
        row_choice = input("\nChoose a row:\n> ")
        try:
            row_choice = int(row_choice)
        except ValueError:
            row_choice = 99
        if row_choice in list(range(1, 11)) and col_choice in COLS.keys():
            if defender_view.board[row_choice - 1][COLS[col_choice]] == MISS or defender_main.board[row_choice - 1][COLS[col_choice]] == HIT:
                clear_screen()
                print("    {}'s Board\n".format(defender.name))
                print(defender_view)
                print('\n')
                print("    {}'s Board\n".format(attacker.name))
                print(attacker_main)
                input("\nYou already fired in that spot! Press ENTER to try again...")
            elif defender_main.board[row_choice - 1][COLS[col_choice]] == EMPTY:
                defender_view.board[row_choice - 1][COLS[col_choice]] = MISS
                clear_screen()
                print("    {}'s Board\n".format(defender.name))
                print('\n')
                print(defender_view)
                print('\n')
                print("    {}'s Board\n".format(attacker.name))
                print(attacker_main)
                input("\nMiss! Please press ENTER and pass the computer to {}.".format(defender.name))
                shooting = False
            elif defender_view.board[row_choice - 1][COLS[col_choice]] == SUNK:
                clear_screen()
                print("    {}'s Board\n".format(defender.name))
                print(defender_view)
                print('\n')
                print("    {}'s Board\n".format(attacker.name))
                print(attacker_main)
                input("\nYou already fired in that spot! Press ENTER to try again...")
            elif defender_main.board[row_choice - 1][COLS[col_choice]] == VERTICAL_SHIP or defender_main.board[row_choice - 1][COLS[col_choice]] == HORIZONTAL_SHIP:
                defender_view.board[row_choice - 1][COLS[col_choice]] = HIT
                defender_main.board[row_choice - 1][COLS[col_choice]] = HIT
                clear_screen()
                print("    {}'s Board\n".format(defender.name))
                print(defender_view)
                print('\n')
                print("    {}'s Board\n".format(attacker.name))
                print(attacker_main)
                input("\nDirect hit! Great job! Hit ENTER to continue...")
                attack = (row_choice-1, COLUMNS.index(col_choice))
                check_for_sink(attack, attacker, defender, attacker_main, defender_main, defender_view)
                shooting = False
            # attack = (row_choice-1, COLUMNS.index(col_choice))
            # hit_and_sink(attack, attacker, defender, attacker_main, defender_main, defender_view)
        else:
            input("\nSorry! You need to choose a row between 1-10 and a column! Try again!")


##########################################################################

def check_for_sink(attack, attacker, defender, attacker_main, defender_main, defender_view):
    # Loop through list of ship objects under Player object
    for key, value in defender.ships.items():
        # Check for presence of attack tuple in each instance of ship.coordinates (a list of tuples)
        # Also check to see if no. of hits is less than length, should skip already sunken ships
        if attack in value.coordinates and value.hits < value.length:
            # Increment hits by one
            value.hits += 1
    # Now that hits have been incremented, loop through defender's ships
    for key, value in defender.ships.items():
        # Check hits against length
        if value.hits == value.length and value.sunk == False:
            # If hits == length, place SUNK at board indexes corresponding with all ship's coordinates
            for i, j in value.coordinates:
                defender_main.board[i][j] = SUNK
            for i, j in value.coordinates:
                defender_view.board[i][j] = SUNK
            sunken = value.name
            value.sunk = True
            clear_screen()
            print("    {}'s Board\n".format(defender.name))
            print(defender_view)
            print('\n')
            print("    {}'s Board\n".format(attacker.name))
            print(attacker_main)
            input("\nWow! Great job {}! You sunk {}'s {}! Press ENTER to continue...".format(attacker.name, defender.name, sunken))


##########################################################################

def check_for_victory(defender, attacker):
    holder = []
    for key, value in defender.ships.items():
        holder.append(value.sunk)
    if len(holder) == 5 and all(p == True for p in holder):
        clear_screen()
        input("All of {}'s ships have been sunk! {} wins!!! Press ENTER to quit...".format(defender.name, attacker.name))
        quit()

##########################################################################

class Player:
    ships = []
    def __init__(self, name):
        self.name= name

##########################################################################

class Ship:
    def __init__(self, name, length, hits=0, coordinates = [], sunk=False):
        self.name = name
        self.length = length
        self.hits = hits
        self.coordinates = coordinates
        self.sunk = sunk


##########################################################################


class Board:
    """Docstring for class Board"""

    # __init__ method designates board, columns, and rows as attributes
    # self.board is the list of lists of EMPTYs that gets manipulated when players place ships
    # self.columns is the top row of letters
    # self.rows is self.board rearranged to look nice in a string
    def __init__(self):
        self.board= [[EMPTY] * len(range(BOARD_SIZE))
                      for number in range(BOARD_SIZE)]
        self.columns= "    " + \
            " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)])

    def make_printable(self, board):
        myobj= enumerate(self.board, start=1)
        output= []
        for index, value in myobj:
            output.append(' {:<2} {}'.format(index, ' '.join(value)))
        return output

    # String magic method - returns strings contained in columns and rows
    # variables

    def __str__(self):
        return self.columns + '\n' + ('\n'.join(self.make_printable(self.board)))



##########################################################################


# Intro and prompt players for names, create Player objects


clear_screen()
input("Welcome to BATTLESHIP! Press ENTER to see the rules...")
clear_screen()
print("""
You have five ships of varying lengths to place
anywhere on the vast open sea before you.
Choose wisely, sailors!\n
Your current fleet, along with each ship's length:\n
Aircraft Carrier, 5 spaces
Battleship, 4 spaces
Submarine, 3 spaces
Cruiser, 3 spaces
Patrol Boat, 2 spaces
""")
input("Press enter to continue...")
clear_screen()
p1_name= input("Please enter the first player's name.\n> ")
clear_screen()
p2_name= input(
    "Welcome, {}!\nPlease enter the second player's name.\n> ".format(p1_name))
p1= Player(p1_name)
p2= Player(p2_name)
p1_board= Board()
p2_board= Board()
p1_enemy_view= Board()
p2_enemy_view= Board()
# p1_tracker = Board()
# p2_tracker = Board()
p1_air = Ship('Aircraft Carrier', 5)
p1_ba = Ship('Battleship', 4)
p1_su = Ship('Submarine', 3)
p1_cr = Ship('Cruiser', 3)
p1_pa = Ship('Patrol Boat', 2)
p2_air = Ship('Aircraft Carrier', 5)
p2_ba = Ship('Battleship', 4)
p2_su = Ship('Submarine', 3)
p2_cr = Ship('Cruiser', 3)
p2_pa = Ship('Patrol Boat', 2)

p1.ships = {'a': p1_air, 'b': p1_ba, 'c': p1_su, 'd': p1_cr, 'e': p1_pa}
p2.ships = {'a': p2_air, 'b': p2_ba, 'c': p2_su, 'd': p2_cr, 'e': p2_pa}




# Display empty board
# Prompt users to place ships
# Validate input
# Update/display updated board

clear_screen()
input("Welcome, {}! Please make sure only {} can see the laptop, then press ENTER...".format(
    p2_name, p1_name))
clear_screen()
choice_getter(p1_board, p1)
clear_screen()
print(p1_board)
input("""
Great job, {}! Now please press ENTER and pass the computer to {} so they can place their ships.
""".format(p1.name, p2.name))
clear_screen()
choice_getter(p2_board, p2)
clear_screen()
print(p2_board)
input("Great job, {}! Please hit ENTER and pass the computer to {} so they can begin their first turn.".format(p2.name, p1.name))
clear_screen()
game_ongoing = True
while game_ongoing:
    turn_taker(p1, p2, p1_board, p2_board, p2_enemy_view)
    check_for_victory(p2, p1)
    turn_taker(p2, p1, p2_board, p1_board, p1_enemy_view)
    check_for_victory(p2, p1)
# Thank you for playing, press enter to quit here.










