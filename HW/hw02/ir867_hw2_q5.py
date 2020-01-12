#hw03
#problem 5

def split_parity(lst):
    for i in range(len(lst)):
        if lst[i]%2==0:
            lst.insert(-1,lst.pop(i))
        else:
            lst.insert(0,lst.pop(i))
    return lst
