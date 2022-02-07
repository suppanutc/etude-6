from carpet import *

def dfs(stock, length):
    """
    Simple depth first search implementation for a Carpet with no matches.
    ---
    PARAMS
    stock : [String]
        A list of strings representing strips in the stock
    length : int
        The desired size of the carpet, i.e. the number of strips needed for the final carpet
    ---
    RETURN
    String
        Either returns a no-match carpet, or if there is no such carpet returns "not possible"
    """

    # stack = []
    stack = [(Carpet([strip])) for strip in stock]
    node = []
    finished = []

    while stack:
        node = stack.pop()
        for child in node.get_children(stock):
           if child.get_total_matches() == 0:
                stack.append(child)
        if node.get_total_matches() == 0 and node.get_length() == length:
            finished = node
            break
        node = []
    if(len(finished) == 0):
        return "not possible"
    return str(finished)

if __name__ == '__main__':
    f = open("large_input.txt", "r", encoding="utf-16")
    contents = f.read()
    stock_list = contents.splitlines()
    f.close()
    found = dfs(stock_list, 50)
    print(found)
