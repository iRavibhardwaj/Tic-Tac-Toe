from Functions import *

# Assigning a number to each position on the game board
positions = {'tl': 1, 'tm': 2, 'tr': 3, 'cl': 4, 'cm': 5, 'cr': 6, 'bl': 7, 'bm': 8, 'br': 9}
print_board(positions)

key_list = list(positions.keys())
val_list = list(positions.values())

player = True
player1 = input("Enter player 1 name --> ").title()
player2 = input("Enter player 2 name --> ").title()
print("Instructions - Enter the number at the position you want to mark")
while True:
    if check_conditions(positions):
        if player:
            print(f"{player2} won the game")
        else:
            print(f"{player1} won the game")
        break
    elif is_full(positions):
        print("Match Draw...")
        break
    if player:
        print(player1, " --> ", end="")
        mark = (input())
        # Trying to convert the input value to integer
        try:
            mark = int(mark)
        except ValueError:
            print("Invalid input")
            continue  # Re-run the loop if input value is not an integer
        if mark not in range(1, 10):
            print("Invalid input")
            continue  # Re-run the loop if input value is not a valid integer
        position = key_list[val_list.index(mark)]
        # Checking weather the position player entered is empty or not
        try:
            positions[position] / 1
        except TypeError:
            print("Invalid move")
        else:
            positions[position] = 'X'
            print_board(positions)
            player = False
    else:
        print(player2, " --> ", end="")
        mark = input()
        try:
            mark = int(mark)
        # Trying to convert the input value to integer
        except ValueError:
            print("Invalid input")
            continue  # Re-run the loop if input value is not an integer
        if mark not in range(1, 10):
            print("Invalid input")
            continue  # Re-run the loop if input value is not a valid integer
        position = key_list[val_list.index(mark)]
        # Checking weather the position player entered is empty or not
        try:
            positions[position] / 1
        except TypeError:
            print("Invalid move")
        else:
            positions[position] = 'O'
            print_board(positions)
            player = True
