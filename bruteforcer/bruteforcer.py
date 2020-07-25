from itertools import combinations, islice
from scipy.special import comb as ncr
import builtins
import numpy as np
from .cy_funcs import get_winners

try:
    builtins.profile
except AttributeError:
    # No line profiler, provide a pass-through version
    def profile(func): return func
    builtins.profile = profile


@profile
def bruteforce(data: list, target: float, max_elems: int, threshold: float) -> list:
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

    # print(f"Will calculate {max_combs} combinations.")

    for group in combs_groups:
        while True:
            batch = list(islice(group, 5000))
            batch_results = np.zeros(len(batch))

            if len(batch) == 0:
                break

            winners += get_winners(batch, batch_results, target, threshold)

    return list(filter(lambda x: len(x) > 0, winners))
