#hw03
#problem 6

def two_sum(lst,target):
    low = 0
    high = len(lst)-1
    while(low<high):
        sum = lst[low] + lst[high]
        if(sum < target):
            low+=1
        elif (sum > target):
            high -=1
        elif(sum==target):
            return (low,high)
    return(None)
