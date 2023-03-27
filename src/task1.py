import random
import numpy as np


def play() -> tuple[bool, int]:
    coins: int = 1
    steps: int = 0

    while 0 < coins < 10:
        steps += 1
        op = random.randint(0, 1)
        if op == 0:
            coins += 1
        else:
            coins -= 1

    return coins == 10, steps


def task1() -> None:
    sample_size: int = 500_000
    win_count: int = 0
    steps_to_lose = []
    steps_to_win = []

    for _ in range(sample_size):
        won, steps = play()
        if won:
            win_count += 1
            steps_to_win.append(steps)
        else:
            steps_to_lose.append(steps)

    print(f'Win probability: {win_count / sample_size}')
    print(f'Average steps to lose: {np.mean(steps_to_lose):.4f}')
    print(f'Average steps to win: {np.mean(steps_to_win):.4f}')
