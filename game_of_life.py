import random


class GameOfLife:

    def __init__(self, **kwargs):
        self.__current_state = GameOfLife.__setup_grid(kwargs)
        self.__grid_size = len(self.__current_state)
        self.__game_over = False

    @staticmethod
    def __setup_grid(kwargs):
        if 'grid' in kwargs.keys():
            grid = kwargs['grid']
            assert len(grid) == len(grid[0])
        else:
            grid = [[random.random() < kwargs['prob_life'] for _ in range(kwargs['grid_size'])] for _ in
                    range(kwargs['grid_size'])]
        return grid

    def is_occupied(self, x, y):
        return self.__current_state[x][y]

    def current_state(self):
        return self.__current_state

    def next_state(self):
        if self.__game_over:
            return None

        next_state = [[False for _ in range(self.__grid_size)] for _ in range(self.__grid_size)]
        for x in range(self.__grid_size):
            for y in range(self.__grid_size):
                num_neighbours = self.count_neighbours(x, y)
                if num_neighbours == 3:
                    next_state[x][y] = True
                if num_neighbours == 2:
                    next_state[x][y] = self.is_occupied(x, y)
        if self.__current_state == next_state:
            self.__game_over = True

        self.__current_state = next_state
        return next_state

    def count_neighbours(self, x, y):
        neighbour_coordinates = [
            [x, self.__prev(y)],  # left
            [x, self.__next(y)],  # right
            [self.__prev(x), y],  # up
            [self.__next(x), y],  # down
            [self.__prev(x), self.__prev(y)],  # left & up
            [self.__prev(x), self.__next(y)],  # right & up
            [self.__next(x), self.__prev(y)],  # left & down
            [self.__next(x), self.__next(y)]  # right & down
        ]
        return [self.is_occupied(x, y) for x, y in neighbour_coordinates].count(True)

    def __prev(self, index):
        return index - 1 if index - 1 >= 0 else index + self.__grid_size - 1

    def __next(self, index):
        return index + 1 if index + 1 < self.__grid_size else index - self.__grid_size + 1

    def print_current_state(self):
        print('-' * (self.__grid_size * 3 + 2))
        for row in self.__current_state:
            print('|', end='')
            for elem in row:
                print(' X ' if elem else ' ∙ ', end='')
            print('|')
        print('-' * (self.__grid_size * 3 + 2))
