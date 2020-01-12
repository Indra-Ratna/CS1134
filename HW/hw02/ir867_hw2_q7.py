#hw02
#problem 7

def findChange(lst01):
    beginning = 0
    last = len(lst01)
    while (beginning <= last):
        mid = (beginning+last)//2
        if(lst01[mid] == 1 and lst01[mid-1]==0):
            return mid
        elif(lst01[mid] < 1):#Left side eliminated
            beginning = mid+1
        else:
            last = mid-1
    return -1
    
