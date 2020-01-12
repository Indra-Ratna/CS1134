#ir867
#hw04

def appearances(s,low,high):
    if(low>high):
        return {}
    final = appearances(s,low+1,high)
    if(s[low] in final):
        final[s[low]]+=1
        return final
    else:
        final[s[low]]=1
        return final
    
