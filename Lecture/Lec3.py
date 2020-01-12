#lec 3
#02/11/19
"""
-to analyze an algorithm find 'maximum contiguous subsequence sum
-use empty set as max sum zero with {} when only negative options for mcss

"""

def func1(num):
    for i in range(num):
        print(i)
    for j in range(num):
        print(j)
def func2(num):
    for i in range(num):
        for j in range(num):
            print(i*j)

#using a table with the amount of work between
#each output u can find how long it takes

def func(n):
    for i in range(n):
        for j in range(n):
            if(i == j):#controlling line of code, running n^2 times.prevents running for loop unless i and j are equal
                for k in range(n):#when this line is in use it changes work, n^2
                    print(i*j*k)#constant that runs n times
#to find maxsum
#ls = {-7,10,9,-5,23,8,-46,4}
#sum(ls from i to j) = sum(lst from i to j-1) + ls[j]
def mcss1(ls):
    maxsum = 0
    for i in range(len(ls)):
        for j in range(i,len(ls)):
            sum = 0
            for k in range(i,j+1):
                sum += ls[k]
            if sum > maxsum:
                maxsum = sum;
    return maxsum;

#n^2, quadratic algorithm
def mcss2(ls):
    maxsum = 0
    for i in range(len(ls)):
        sum = 0
        for j in range(i, len(ls)):
            sum += ls[j]
            if sum > maxsum:
                maxsum = sum;
    return maxsum;
