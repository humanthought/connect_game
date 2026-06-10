"""
connect_game.py
This script will start the connect game.

AI disclosure: Initial code did not include type hints. Type hints were added by cursor.
"""

import sys
from typing import NoReturn

from grid import Grid
import constants as c


def non_numerical_entry_detected() -> NoReturn:
    print('Non-numerical entry detected. Exit game.')
    sys.exit(1)


def main() -> None:
    
    print('Welcome to the connect game. Please note that entering any non-numerical entry will end the game.')
    
    request_size_input = True
    while request_size_input:
        try:
            size = int(input(f'Enter size of board {c.MIN_SIZE} - {c.MAX_SIZE}: '))
        except ValueError:
            non_numerical_entry_detected()   
     
        request_size_input = not Grid.is_grid_within_size_limit(size)
        

    g = Grid(size) 
    try:
        win_length = int(input('Enter length required to win: '))
    except ValueError:
        non_numerical_entry_detected() 

    print(f"Here's the board of size: {size}")

    g.print_grid()
    continue_game = True
    continue_player1_move = True
    continue_player2_move = True
    while continue_game:
        while continue_player1_move:
            try:
                player1_x_pos = int(input('Player 1, enter x position: '))
                player1_y_pos = int(input('Player 1, enter y position: '))
                continue_player1_move = not g.assign_position(1, player1_x_pos, player1_y_pos)
                g.print_grid()
                if g.get_max_length(1) == win_length:
                    print('Player 1 wins!')
                    sys.exit(0)
            except ValueError:
                non_numerical_entry_detected() 

        while continue_player2_move:
            try:
                player2_x_pos = int(input('Player 2, enter x position: '))
                player2_y_pos = int(input('Player 2, enter y position: '))
                continue_player2_move = not g.assign_position(2, player2_x_pos, player2_y_pos)
                g.print_grid()
                if g.get_max_length(2) == win_length:
                    print('Player 2 wins!')
                    sys.exit(0)

            except ValueError:
                non_numerical_entry_detected() 
        
        continue_player1_move = True
        continue_player2_move = True

if __name__ == "__main__":
    main()
