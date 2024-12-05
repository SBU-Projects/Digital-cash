"""from functions.initialization import Initialization
from functions.bank import Bank

init1 = Initialization(28871271685163)
bank1 = Bank("Dr.Ziba Eslami", init1.get_public_arguments())"""


def generate_partitions(m, n, current_partition=[], start=1):
    # Base case: If we need 1 part, the only valid partition is the remaining value
    if n == 1:
        if m >= start:
            return [current_partition + [m]]
        else:
            return []

    # Recursive case: Generate partitions
    partitions = []
    for first in range(start, m - n + 2):  # Ensure non-decreasing order by using `start`
        partitions += generate_partitions(m - first, n - 1, current_partition + [first], first)
    return partitions


# Example usage
m = 6
n = 2
partitions = generate_partitions(m, n)
print(f"Partitions of {m} into {n} parts:", partitions)

