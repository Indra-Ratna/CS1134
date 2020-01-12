#ir867
#hw04

def split_by_sign(lst,low,high):
    if(low==high):
        return[]
    if(lst[low]>0):
        return [lst[low]]+split_by_sign(lst,low+1,high)
    else:
        return split_by_sign(lst,low+1,high)+[lst[low]]
