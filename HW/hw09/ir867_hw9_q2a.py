#hw9 q2a
def intersection_list(lst1,lst2):
    lst1.sort()
    lst2.sort()
    intersects = []
    i = 0
    j = 0

    while i<len(lst1) and j<len(lst2):
        if j<len(lst2) and lst2[j]<lst1[i]:
            j+=1
        elif lst1[i] == lst2[j]:
            intersects.append(lst1[i])
            i+=1
            j+=1
        else:
            i+=1
    return intersects
