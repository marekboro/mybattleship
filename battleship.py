from random import randint
import sys

board1 = []


def set_board_size1(width, height):
    the_width = []
    for a in range(0, the_width):
        width.append("O")

        for b in range(0, height):
            # board.append(["O","O","O","O","O"])
            board.append(the_width)


def get_board_dimentions():
    print("something")


def print_board1(board_name):
    the_board = boardname


# ONLY CODE FROM CODE-ACADEMY:

# FUNCTIONS
def print_logo():
    print("")
    print("- - - - - - - B - A - T - T - L - E - - - S - H - I - P - S - - - - - - -")
    print("")



board = []

#board = set_board_size(10,10)
def set_board_size(width, height):
    created_board = []
    board_width = []
    for i in range(0,width):
        #print("a")
        board_width.append("O")
    for i in range(0,height):
        #print("b")
        created_board.append(board_width)
    print(width)
    print(created_board)
    return created_board



#for i in range(0, 5):
#    board.append(["O", "O", "O", "O", "O"])


def print_board(board_in):
    for i in range(0, len(board_in)):
        print("  ".join(board[i]))
        # print(board_in[i])


#test
new_board = set_board_size(10,10)
print_board(new_board)


def random_row(board_in):
    return randint(0, len(board_in) - 1)


def random_col(board_in):
    return randint(0, len(board_in) - 1)


# def check_shot(x_coordinate,y_coordiante,a_board):
#     a_board = board
#     x_coordinate = guess_row
#     y_coordiante = guess_col
#     if


# PROGRAM CODE:
# 001 START : simulate 1st attack as a hit:
#board[1][1] = "X"

# 001 END
#print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

guess_row =0    #
guess_col =0    #

all_team_ships_destroyed = False
game_turns = 4

# def ask_for_input():
#     print(f"Ship is in ROW: {ship_row}")
#     print("")
#     global guess_row
#     guess_row = int(input("Guess Row: "))
#     print(f"Ship is in COLUMN: {ship_col}")
#     print("")
#     global guess_col 
#     guess_col = int(input("Guess Column: "))

   
def ask_for_input():
    global guess_row
    #guess_row =0
    global guess_col
    #guess_col =0
    obtain_int_row = False
    obtain_int_col = False
    print(f"Ship is in ROW: {ship_row} and column {ship_col}")
    print("")
    #guess_row = int(input("Guess Row: "))
    while obtain_int_row==False:
        guess_row_string = input("Guess Row: ")
        if guess_row_string.isdigit():
            guess_row = int(guess_row_string)
            obtain_int_row = True
    while obtain_int_col==False:
        guess_col_string = input("Guess Column: ")
        if guess_col_string.isdigit():
            guess_col = int(guess_col_string)
            obtain_int_col = True

# print(f"{ship_row}")
# guess_row = int(input("Guess Row: "))
# print(f"{ship_col}")
# guess_col = int(input("Guess Column: "))



for turn in range(0,game_turns):
    if all_team_ships_destroyed == False:
        print_board(board)
        print("")
        print(f"Turn: {turn +1}")
        print("")
        ask_for_input()
        print("INPUT REQUESTED")
        if guess_row not in range(len(board)) or guess_col not in range(len(board[guess_row])):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sank my battleship")
                board[guess_row][guess_col] = "X"
                all_team_ships_destroyed = True
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            
print_board(board)
print("State of board at END")

# for turn in range(0,4):
#     print_board(board)
#     print("")
#     print(f"Turn: {turn +1}")
#     print("")
#     ask_for_input()
#     print("INPUT REQUESTED")
#     if guess_row not in range(len(board)) or guess_col not in range(len(board[guess_row])):
#         print("Oops, that's not even in the ocean.")
#     elif board[guess_row][guess_col] == "X":
#         print("You guessed that one already.")
#     else:
#         if guess_row == ship_row and guess_col == ship_col:
#             print("Congratulations! You sank my battleship")
#             board[guess_row][guess_col] = "X"
#         else:
#             print("You missed my battleship!")
#             board[guess_row][guess_col] = "X"
            
# print_board(board)
# print("State of board at END")



