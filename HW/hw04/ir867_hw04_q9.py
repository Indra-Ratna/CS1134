#ir867
#hw04

def permutations(lst,low,high):
    if low==high:
        return [[lst[low]]]
    out = []
    for i in range(low,high+1):
        lst[i],lst[low]=lst[low],lst[i]
        for j in permutations(lst,low+1,high):
            rest =[lst[low]]+j
            out.append(rest)
        lst[i],lst[low]=lst[low],lst[i]
    return out
