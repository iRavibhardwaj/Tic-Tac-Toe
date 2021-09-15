def print_board(board):
    """Prints the game layout."""
    layout = (f" {board['tl']} | {board['tm']} | {board['tr']} \n___|___|___\n"
             f" {board['cl']} | {board['cm']} | {board['cr']} \n___|___|___\n"
             f" {board['bl']} | {board['bm']} | {board['br']} ")
    print(layout)


def check_conditions(board):
    """Returns True if either or the player fulfilled the winning conditions"""
    if (board['tl'] == board['tm'] == board['tr'] or
            board['cl'] == board['cm'] == board['cr'] or
            board['bl'] == board['bm'] == board['br'] or
            board['tl'] == board['cl'] == board['bl'] or
            board['tm'] == board['cm'] == board['bm'] or
            board['tr'] == board['cr'] == board['br'] or
            board['tl'] == board['cm'] == board['br'] or
            board['tr'] == board['cm'] == board['bl']):
        return True
    return False


def is_full(board):
    """Returns True if all the positions on the board are marked"""
    for i in range(1, 10):
        if i in board.values():
            return False
    return True
