import random
import numpy as np


def studied(num: int):
    return 0 <= num < 20


def play(second: bool = False) -> bool:
    tickets = list(range(30))

    if second:
        ch = random.choice(tickets)
        tickets.remove(ch)

    ch = random.choice(tickets)
    return ch < 20


def task3():
    sample_size: int = 1_000_000

    success_first: int = 0
    success_second: int = 0

    for _ in range(sample_size):
        if play():
            success_first += 1
        if play(second=True):
            success_second += 1

    print(f'First, success chance: {success_first / sample_size}')
    print(f'First, success chance: {success_second / sample_size}')


if __name__ == '__main__':
    task3()
