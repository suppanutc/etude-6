from collections import deque

def greedy(stock, size):
    """
    Simple greedy algorithm to get a lower bound for a maximal carpet.
    ---
    PARAMS
    stock: [String]
        a list of strings(strips) representing the stock
    size: int
        the number of strips needed in the carpet
    ---
    RETURN
    Carpet
        returns a Carpet
    """
    temp_stock = stock.copy() #remove strips from temp_stock when we add to the greedy carpet
    greedyCarpet = list()
    greedyCarpet.append(temp_stock[0])
    temp_stock.pop(0)
    #Build the carpet strip by strip, picking the most matches each time
    while len(greedyCarpet) < size:
        temp_strip = temp_stock[0]
        for strip in temp_stock:
            if (potential_matches(greedyCarpet, strip) > potential_matches(greedyCarpet, temp_strip)):
                temp_strip = strip
        greedyCarpet.append(temp_strip)
        temp_stock.remove(temp_strip)
    return greedyCarpet

def maximal_carpet(stock, size):
    max_carpet = greedy(stock, size) 
    max_matches = total_matches(max_carpet)
    #If we don't have any possible matches within our stock, just return our greedy carpet
    if max_matches == 0:
        return max_carpet 
    # print(f"Max Greedy Matches: {max_matches}")

    visited = {}
    stack = deque()
    for strip in stock:
        strips = []
        strips.append(strip)
        stack.append(strips)
        visited[strip] = None
    current_carpet = []
    strip_length = len(stock[0]) #all strips should be the same size

    while stack:
        current_carpet = stack.pop()
        total = total_matches(current_carpet)
        print(f"Current Carpet {current_carpet}")
        #Is it better than our current max carpet?
        if total_matches(current_carpet) > max_matches:
                max_carpet = current_carpet
                max_matches = total_matches(current_carpet)
                print(f"New max {max_carpet}")
        if len(current_carpet) >= size:
            print(f"Oversized/complete {current_carpet}")
            continue
        if perfect_matches(current_carpet,size,strip_length,total) <= max_matches:
             print(f"Already worse: {current_carpet}")
             continue
        
        #Generate child nodes
        temp_stock = stock.copy()
        for strip in current_carpet:
            temp_stock.remove(strip)   
        used_strips = visited.get(current_carpet[-1])
        if used_strips is None:
            for strip in temp_stock:
                used_strips = list()
                used_strips.append(strip)
                node = {current_carpet[-1] : used_strips}
                visited.update(node)
                child = current_carpet.copy()
                child.append(strip)
                print(f"Child {child}")
                stack.append(child)
            continue
        for strip in temp_stock:
            if strip not in current_carpet and strip in used_strips: #todo: fix this!!!!!!
                print(f"Strip not in current, but already in used {current_carpet}")
                continue
            elif strip not in current_carpet:
                used_strips.append(strip)
                node = {current_carpet[-1] : used_strips}
                visited.update(node)
            #if we would have perfect matches from this strip on, would it already be worse?
            if (total + strip_length * (size - len(current_carpet) +1)) <= max_matches:
                continue
            child = current_carpet.copy()
            child.append(strip)
            stack.append(child)
            print(f"Child {child}")

    return max_carpet


def perfect_matches(carpet,size, strip_length, total):
    """
    Computes the amount of matches the carpet could get if all of the remaining strips were fully matching.
    ---
     PARAMS
    carpet: Carpet
        the Carpet object to find the perfect matches of
    size: int
        the length the carpet should be at the end
    strip_length: int
        the length of the strips
    ---
    RETURN
    int
        the potential number of matches for a perfect carpet
    """
    remaining_strips = size - len(carpet)
    return total + strip_length * remaining_strips

def total_matches(carpet):
    total_matches = 0
    for index in range (len(carpet)-1):
        total_matches += find_matches(carpet[index], carpet[index+1])
    return total_matches

def potential_matches(carpet, strip):
    return total_matches(carpet) + find_matches(carpet[-1],strip)

def find_matches(strip_1, strip_2):
    matches = 0
    for index in range(len(strip_1)):
        if index >= len(strip_2):
            continue
        if strip_1[index] == strip_2[index]:
            matches = matches + 1
    return matches

if __name__ == '__main__':
    stock = ["AAB", "BBB", "ABB", "CBA", "CCC", "CBC", "CBB", "BAB", "CCA", "CCB", "CCC", "CCC"]
    found1 = greedy(stock, 5)
    found2 = maximal_carpet(stock, 5)
    print("---")
    print(found1)
    print(total_matches(found1))
    print("---")
    print(found2)
    print(total_matches(found2))
