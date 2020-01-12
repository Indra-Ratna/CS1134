#hw9 q2b
from ChainingHashTableMap import ChainingHashTableMap

def intersection_list(lst1, lst2):
    hash = ChainingHashTableMap()
    intersects = []

    for elem in lst1:
        hash[elem] = i

    for item in lst2:
        try:
            if hash[item] is not None:
                if hash[item] == i:
                    intersects.append(item)
        except:
            pass
    return intersects
