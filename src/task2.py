import random
from typing import Dict
from matplotlib import pyplot as plt  # type:ignore

import numpy as np


def throw():
    return random.randint(0, 7), random.randint(0, 7)


def play() -> Dict[int, int]:
    field = np.zeros([8, 8], dtype=np.int64)
    for _ in range(64):
        field[throw()] += 1

    seed_counts, cell_counts = np.unique(field, return_counts=True)
    return dict(zip(seed_counts, cell_counts))


def task2():
    data = np.zeros(65)
    sample_size: int = 50_000

    for _ in range(sample_size):
        for seeds, cells in play().items():
            data[seeds] += cells

    std = np.std(data)

    plt.bar(
        np.arange(0, 65, 1, dtype=np.int64),
        data / sample_size
    )
    plt.xlim(-1, 10)
    plt.xticks(range(10), range(10))
    plt.show()


if __name__ == '__main__':
    task2()
