# cython: language_level=3
# cython: boundscheck=False

import numpy as np

def get_winners(batch, batch_results, int target):
    winners = []
    cdef int i, x

    for i, combination in enumerate(batch):
        batch_results[i] = abs(sum(x[1] for x in combination) - target)

    indexes = np.where(batch_results <= 10)[0]
    for x in indexes:
        winners.append((batch[x], batch_results[x]))

    return winners