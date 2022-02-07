
from carpet import *
from collections import deque

class Balanced:
    
    def balanced_carpet(stock, size):
        #seen = set()
        stack = deque()
        potential_carpet = []
        max_matches = (size - 1) * len(stock[0])
        no_matches = 0
        ideal = max_matches / 2 #ideal number of matches, this has to be determined in main?

        for strip in stock: #add initial one strip long carpet
            strips = []
            strips.append(strip)
            carpet_new = Carpet(strips)
            stack.append(carpet_new)

        while stack: #while stack not empty
            current_carpet = stack.pop()
            #print(f"popped: {popped}")
            #print(f"popped type: {type(popped)}")
            #seen.add(strips) #problem here, cant add list to set
            if current_carpet.length is not size: 
                #if the current list popped from stack is not the size we looking for then
                #keep finding its neighbours and add to stack
                neighbours = current_carpet.get_children(stock)
                #print(f"neighbour: {neighbours}")
                for a_neighbour in neighbours:
                    #print(f"a_neighbour: {a_neighbour}")
                    stack.append(a_neighbour)
            else:
            #for now if its not max matches or no matches then just add to potential_carpet
                if current_carpet.get_total_matches is ideal or ideal-1 or ideal+1:
                    #if (strips not in seen):
                    potential_carpet.append(current_carpet)
                    

        ideal = max_matches / 2 #ideal number of matches, this has to be determined in main?
        print(f"potential_carpet: {potential_carpet}")

        #for x in range(ideal-1):
            #ideal_upper = ideal + x
            #ideal_lower = ideal - x
            #for strip in potential_carpet:
              #  _carpet = Carpet(strip)
              #  if _carpet.get_total_matches is ideal_lower or ideal_upper:
              #      return _carpet

       # return "Not found"



    if __name__ == '__main__':
        stock = ["AAB", "BBB", "ABB", "CBA", "CCC", "CBC", "CBB", "BAB", "CCA", "CCB", "CCC", "CCC"]
        new_carpet = Carpet(['ABB', 'CCA', 'CBA', 'BBB', 'CCC'])
        #print(new_carpet)
        #length = new_carpet.get_length
        #print(f"length: {length}")
        #print(f"len: {new_carpet.length}")
        #balanced_carpet(stock, 5)
        