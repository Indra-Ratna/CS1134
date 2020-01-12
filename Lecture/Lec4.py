#lec 4
#02/13/19
"""
for run time look for
    best case
    worst case
    average case
    amortized average case
"""
def mcss3(ls):
    sum = 0
    maxsum = 0
    for i in range(len(ls)):
        sum += ls[i]
        if sum > maxsum:
            maxsum = sum
        elif sum < 0:
            sum = 0
    return maxsum

def find(ls,item):
    for i in range(len(ls)):
        if ls[i] == item:
            return i
    return -1
"""
^ linear search
for run time look for
    best case: O(1)
    worst case: O(N)
    average case: O(N)
    amortized average case: O(N)
    
"""
def binary_search(ls,item):
    start = 0
    end = len(ls)
    while (start <= end):
        mid = (start+end)//2
        if(ls[mid] == item):
            return mid
        elif(ls[mid] < item):#Left side eliminated
            start = mid+1
        else:
            end = mid-1
    return -1
"""
f(n) = f(n-1) + f(n-2)
f(0) = 1
f(2) = 1
"""
def fib(n):
    if(n<2):
        return 1;
    return fib(n-1) + fib(n-2);
#O(2^n) exponential, a lot of work for a computer
