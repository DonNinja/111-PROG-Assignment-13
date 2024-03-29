# Gihub Repo: https://github.com/DonNinja/111-PROG-Assignment-13
# Þeir sem unnu þetta saman voru: Yngvi Leó Þráinsson, Magnús Friðrik Helgason & Nökkvi Már Nökkvason

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
COINMESSAGE = "Pull a lever (y/n): "

def main():
    play = True
    while play == True:
        victory = False
        row = 1
        col = 1
        total_coins = 0

        valid_directions = NORTH
        print_directions(valid_directions)

        while not victory:
            victory, col, row = play_one_move(col, row, valid_directions)
            if victory:
                print("Victory! Total coins", str(total_coins) + ".")
                pa_input = input('Play again (y/n): ')
                play = play_again(pa_input)
            else:
                total_coins = coinMessage(col, row, total_coins)
                valid_directions = find_directions(col, row)
                print_directions(valid_directions)

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true is player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row

def coinMessage(col, row, total_coins):
    prev_coin = total_coins
    if col == 1 and row == 2:
        answer = input(COINMESSAGE)
        total_coins = get_coin(answer, total_coins)
    elif col == 2 and row == 2:
        answer = input(COINMESSAGE)
        total_coins = get_coin(answer, total_coins)
    elif col == 2 and row == 3:
        answer = input(COINMESSAGE)
        total_coins = get_coin(answer, total_coins)
    elif col == 3 and row == 2:
        answer = input(COINMESSAGE)
        total_coins = get_coin(answer, total_coins)
    if prev_coin != total_coins:
        print("You received 1 coin, your total is now", str(total_coins) + ".")
    return total_coins

def get_coin(answer, total):
    if answer.lower() == "y":
        total += 1
        return total
    else:
        return total 

def play_again(pa_input):
    if pa_input.lower() == 'y':
        return True
    else:
        return False
    
# The main program starts here
main()
