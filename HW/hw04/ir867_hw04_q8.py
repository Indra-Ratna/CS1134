#ir867
#hw04

def flat_list(nested_lst,low,high):
    if(low>high):
        return []
    out = []
    if(isinstance(nested_lst[low],int)):
        out.append(nested_lst[low])
    else:
        out+=flat_list(nested_lst[low],0,(len(nested_lst[low])-1))
    out+= flat_list(nested_lst,low+1,high)
    return out
