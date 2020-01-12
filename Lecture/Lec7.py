#lec 3/11
#sorting algorithms

"""
-dont need to know all the sorting algorithm

-for worst case would not consider amortized

-if runtime is n but could be 1, explain why

-repeating halfing for finding an element is big theta(logN) base 2 runtime

-if searching by jumping root n values for atleast 1000 elements
then the jump search finds a higher value and searches vack for a
runtime of big theta (root(n))

-how much each loop costs and how much you are running each loop

-explain space, draw memory map

-writing methods in classes could be on the exam[prob isnt]
"""

def q3():
    lst = [-1,1,4,-2,-3]
    #result = [i for i in range(len(lst)-1) if prefix_sum(lst,i)>0]

    res = [i for i in range(len(lst)-1) if sum(lst[:i+1])>0]
    return res

    #poor performance ^^
    #sum runs at theta(n)
print(q3())



"""SORTING ALGORITHMS
-selection,insertion,bubble,merge,quick,heap...
-^^puts things in ascending order

-Selection sort
    -use current and find minimum in list theta(n)
    -then swap elements by swapping current with minimum
    -n operation by finding minimum and wapping with current
    -theta(n^2) algorithm based on best and worst case

-Insertion sort
    -a single element alone is always sorted
    -move pointer up one element and decide if lower element is meant to be ther
    -using another element, insert each additional elemeent inot sorted array
    at appropriate location
    -
-between selectio and insertion selection would always be theta(n)
-time complexity selection: T(n) + n+(n-1)+(n-2) for theta(n^2)
-time cpmplexity insertion T(N)+1+2+3+...(N-2)+(n-1) for theta9N^2)
-best case scenario for lsts is havinga sorrted array
-if u give insertion sort a sorted list, it is created in theta(n) rdprvislly ig lsdy
vhstsvyrtid lrdd yhsn nre opyion.

-Merge sort
    -sort first half revursively
    -sort second half recursively
    0merge two ahalves into one sorted sequence for theta(n)
    -betwwen both lists, one o the mins has to be the minimumelement'
    -how many levels if n opearation for each number

level #
#cost of calls in level
$coh of each call in level*total cost of level theta(9),`,n,n
_by this logic it ends as n
-guarnteed how fast it is in runtime but find out how many peolep in hall by diving by
3 eafh tiem. 

-log base 2(million) = 20

merge sort is theta(nlogn) which is much better than theta(n^2

"""
