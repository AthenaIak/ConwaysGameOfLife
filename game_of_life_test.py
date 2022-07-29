import unittest

from game_of_life import GameOfLife


class StateTest(unittest.TestCase):
    def test_init(self):
        grid = [[True, False, True], [False, False, False], [True, False, True]]
        state = GameOfLife(grid=grid)
        self.assertEqual(state.current_state(), grid)

        self.assertIsNotNone(GameOfLife(grid_size=5, prob_life=0.5))

        with self.assertRaises(KeyError):
            GameOfLife(grid_size=5)

        with self.assertRaises(KeyError):
            GameOfLife(prob_life=0.5)

        with self.assertRaises(AssertionError):
            bad_grid = [[True, False, True], [False, False, False]]
            GameOfLife(grid=bad_grid)

    def test_is_occupied(self):
        state = GameOfLife(grid=[[True, False], [False, False]])
        self.assertTrue(state.is_occupied(0, 0))
        self.assertFalse(state.is_occupied(0, 1))

    def test_count_neighbours(self):
        grid = [[True, False, True], [False, False, False], [True, False, True]]
        state = GameOfLife(grid=grid)
        self.assertEqual(state.count_neighbours(0, 0), 3)
        self.assertEqual(state.count_neighbours(0, 2), 3)
        self.assertEqual(state.count_neighbours(2, 0), 3)
        self.assertEqual(state.count_neighbours(2, 2), 3)
        self.assertEqual(state.count_neighbours(1, 1), 4)

    def test_next_state(self):
        # 4 neigh and alive -> dead
        # 3 neigh and dead  -> alive
        grid = [[False for _ in range(5)] for _ in range(5)]
        grid[1][1] = grid[3][1] = grid[1][3] = grid[3][3] = grid[2][2] = True
        state = GameOfLife(grid=grid)
        state.next_state()
        grid = [[False for _ in range(5)] for _ in range(5)]
        grid[1][2] = grid[2][1] = grid[2][3] = grid[3][2] = True
        self.assertEqual(state.current_state(), grid)

        # 4 neigh and dead  -> dead
        grid = [[False for _ in range(5)] for _ in range(5)]
        grid[1][1] = grid[3][1] = grid[1][3] = grid[3][3] = True
        state = GameOfLife(grid=grid)
        state.next_state()
        grid = [[False for _ in range(5)] for _ in range(5)]
        self.assertEqual(state.current_state(), grid)

        # 3 neigh and alive -> alive
        # 3 neigh and dead  -> alive
        # 2 neigh and alive -> alive
        # 2 neigh and dead  -> dead
        grid = [[False for _ in range(5)] for _ in range(5)]
        grid[1][1] = grid[2][2] = grid[2][3] = grid[3][2] = True
        state = GameOfLife(grid=grid)
        state.next_state()
        grid = [[False for _ in range(5)] for _ in range(5)]
        grid[1][2] = grid[2][1] = grid[2][2] = grid[2][3] = grid[3][2] = grid[3][3] = True
        self.assertEqual(state.current_state(), grid)

        # 1 neigh and alive -> dead
        grid = [[False for _ in range(5)] for _ in range(5)]
        grid[1][1] = grid[2][1] = True
        state = GameOfLife(grid=grid)
        state.next_state()
        grid = [[False for _ in range(5)] for _ in range(5)]
        self.assertEqual(state.current_state(), grid)


if __name__ == '__main__':
    unittest.main()
