import fileinput

from carpet import Carpet
import random
from math import factorial

# This defines the maximum amount of times to loop
GLOBAL_MAX = 250000


# This mathematics formular finds how many combinations are there for {size} items
# in {num_items} pool. This does not take the ordering into consideration.
# so 10 num_items with 10 size will produce only 1 unique combination
def max_comb(num_items, size):
    return factorial(num_items) / (factorial(num_items - size) * factorial(size))


def randomize_carpet(stock, size):
    return random.sample(list(stock), size)


def balanced_random(stock, size):
    best_carpet = Carpet(randomize_carpet(stock, size))
    best_carpet_abs = best_carpet.get_total_matches()
    target_match = int((len(stock[0]) * (size - 1)) / 2)
    # print(f"target match: {target_match}")
    if max_comb(len(stock), size) <= GLOBAL_MAX:
        max_count = int(max_comb(len(stock), size))
    else:
        max_count = int(GLOBAL_MAX)
    # print(f"max count: {max_count}")
    # print(f"target match: {target_match}")
    for x in range(max_count):
        new_carpet = Carpet(randomize_carpet(stock, size))
        new_carpet_matches = new_carpet.get_total_matches()
        # print(f"current new_carpet = {new_carpet}, matches: {new_carpet_matches}")
        if abs(target_match - new_carpet_matches) < abs(target_match - best_carpet_abs):
            best_carpet = new_carpet
            best_carpet_abs = new_carpet_matches

    # print(f"Best Carpet: {best_carpet}, matches: {best_carpet_abs}")
    return best_carpet


if __name__ == '__main__':
    # stock = ["AAB", "BBB", "ABC", "CBA", "CCC", "CBC", "CBB", "BAB", "CCA", "CCB", "BAC", "AAA", "BCC", "CAB", "BCA"]
    f = open("large_input.txt", "r", encoding="utf-16")
    contents = f.read()
    stock = contents.splitlines()
    f.close()
    result = balanced_random(stock, 5)
    print(f"Best Carpet:\n{result} \nMatches: {result.get_total_matches()}")

    # new_carpet = Carpet(['ABB', 'CCA', 'CBA', 'BBB', 'CCC'])
