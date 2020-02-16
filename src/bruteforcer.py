from itertools import combinations, islice
from scipy.special import comb as ncr
import builtins
import numpy as np
from numba import jit

try:
    builtins.profile
except AttributeError:
    # No line profiler, provide a pass-through version
    def profile(func): return func
    builtins.profile = profile


@profile
def bruteforce(data: list, target: float, max_elems: int) -> list:
    winners = []

    # Filter down data to remove zeros
    data_len = len(data)
    data = list(filter(lambda x: x[1] != 0, data))
    target = abs(target)

    combs_groups: list = []
    max_combs: int = 0

    for x in range(1, max_elems+1):
        combs_groups.append(combinations(data, x))
        max_combs += ncr(data_len, x)

    print(f"Will calculate {max_combs} combinations.")

    for group in combs_groups:
        while True:
            batch = list(islice(group, 5000))
            batch_results = np.zeros(len(batch))

            if len(batch) == 0:
                break

            for i, combination in enumerate(batch):
                batch_results[i] = abs(sum(x[1] for x in combination) - target)

            indexes = np.where(batch_results <= 10)[0]
            for x in indexes:
                winners.append((batch[x], batch_results[x]))

    return list(filter(lambda x: len(x) > 0, winners))
