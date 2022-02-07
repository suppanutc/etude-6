from carpet import *
from dfsV2 import *
from greedy import *
from maximal import *
import time


# Run with: $ cat input.txt | python main.py

def main():
    stock = list()
    while True:
        try:
            stock.append(input())
        except Exception:
            break

    start = time.time()
    found = greedy(stock, 10)
    #found = dfs_pruning(stock, 10)
    found = maximal_carpet(stock, 10)
    end = time.time()
    print(found)
    print(total_matches(found))
    #print(found.get_total_matches())

    print(f"Elapsed: {end-start}")

if __name__ == "__main__":
    main()