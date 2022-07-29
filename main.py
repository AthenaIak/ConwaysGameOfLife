from game_of_life import GameOfLife
import time


def run_game_of_life(grid_size, prob_life, max_iterations):
    game_of_life = GameOfLife(grid_size=grid_size, prob_life=prob_life)

    print("State 0")
    game_of_life.print_current_state()

    curr_iteration = 1
    while game_of_life.next_state() and curr_iteration < max_iterations:
        # adding time delay of half second
        time.sleep(0.3)

        print("State %d" % curr_iteration)
        game_of_life.print_current_state()
        curr_iteration += 1


if __name__ == '__main__':
    run_game_of_life(grid_size=16, prob_life=0.4, max_iterations=150)
