import numpy as np
import constants as c

class Grid:

    def __init__(self, size):
        self.size = size
        self.grid_array = np.zeros((self.size, self.size), dtype=int)
        self.player1_positions = []
        self.player2_positions = []
        self.player1_max_length = 1
        self.player2_max_length = 2

    def print_grid(self):

        for j in range(self.size):
            for i in range(self.size):
                if self.grid_array[i, j] != 0:
                    print(f'   {self.grid_array[i, j]}  ', end=" ") 
                else:
                    print(f'({i}, {j})', end=" ")
            print()
        
        print("##########################")

        """ 
        Print statements for debugging
        print(f'Player 1 positions: {self.player1_positions}')
        print(f'Player 2 positions: {self.player2_positions}')
        """
        return True
    
    @staticmethod
    def is_grid_within_size_limit(size):
        if size < c.MIN_SIZE:
            print(f'size: {size} < min size: {c.MIN_SIZE}')
            return False
        elif size > c.MAX_SIZE:
            print(f'size: {size} > max size: {c.MAX_SIZE}')
            return False
        else:
            return True

    def _is_position_within_size_limit(self, position):
        if position > self.size - 1:
            print(f'Position: {position} exceeds size - 1')
            return False
        elif position < 0:
            print(f'Position: {position} of negative value is not valid.')
            return False
        else:
            return True

    def assign_position(self, player, x, y):
        
        return_val = True
       
        x_position_within_size_limit = self._is_position_within_size_limit(x)
        y_position_within_size_limit = self._is_position_within_size_limit(y)

        if not x_position_within_size_limit:
            print(f'Invalid x position. Player {player} redo x position.')
            return_val = False

        if not y_position_within_size_limit:
            print(f'Invalid y position. Player {player} redo y position.')
            return_val = False

        if x_position_within_size_limit and y_position_within_size_limit:
            
            if self.grid_array[x, y] == 0: 
                self.grid_array[x, y] = player
                if player == 1:
                    self.player1_positions.append((x, y))
                    self.player1_positions = sorted(self.player1_positions)
                else:
                    self.player2_positions.append((x, y))
                    self.player2_positions = sorted(self.player2_positions)
                return_val = True
            else: 
                print(f'Location ({x}, {y}) is occupied')
                return_val = False
 
        return return_val

    def _get_max_count_right(self, player, positions):
       
        max_count_right = 1   
        
        for position in positions:
            for count_right in range(1, self.size):
                if (position[0] + count_right, position[1]) in positions:
                    if count_right >= max_count_right:
                        max_count_right = count_right + 1
                else:
                    break

        return max_count_right

    def _get_max_count_down(self, player, positions):
       
        max_count_down = 1   
        
        for position in positions:
            for count_down in range(1, self.size):
                if (position[0], position[1] + count_down) in positions:
                    if count_down >= max_count_down:
                        max_count_down = count_down + 1
                else:
                    break

        return max_count_down

    def _get_max_count_diagonal_down(self, player, positions):
        max_count_diagonal_down = 1   
        
        for position in positions:
            for count_diagonal_down in range(1, self.size):
                if (position[0] + count_diagonal_down, position[1] + count_diagonal_down) in positions:
                    if count_diagonal_down >= max_count_diagonal_down:
                        max_count_diagonal_down = count_diagonal_down + 1
                else:
                    break

        return max_count_diagonal_down

    def _get_max_count_diagonal_up(self, player, positions):
        max_count_diagonal_up = 1   
        
        for position in positions:
            for count_diagonal_up in range(1, self.size):
                if (position[0] - count_diagonal_up, position[1] - count_diagonal_up) in positions:
                    if count_diagonal_up >= max_count_diagonal_up:
                        max_count_diagonal_up = count_diagonal_up + 1
                else:
                    break

        return max_count_diagonal_up

    def get_max_length(self, player):
        
        if player == 1:
            positions = self.player1_positions
        else:
            positions = self.player2_positions

        max_length = max(self._get_max_count_right(player, positions),  
                         self._get_max_count_down(player, positions), 
                         self._get_max_count_diagonal_down(player, positions),  
                         self._get_max_count_diagonal_up(player, positions)) 
        
        #Below print statement for debugging 
        #print(f'Player {player} max length: {max_length}')
        return max_length

