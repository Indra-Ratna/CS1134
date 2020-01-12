#question 2b
def shift(lst,k,position = "left"):
    move = len(lst)-1
    place = 0
    if(position =="left"):
        move = 0
        place = len(lst)-1
    for i in range(k):
        lst.insert(place,lst.pop(move))
    return lst
