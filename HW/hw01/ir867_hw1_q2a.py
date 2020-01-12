#question 2a
def shift(lst,k,):
    move = 0
    place = len(lst)-1
    for i in range(k):
        lst.insert(place,lst.pop(move))
    return lst
