#Indra Ratna
#Question 3
#HW 3

def find_duplicates(lst):
    lst.sort()
    acc = []
    for i in range (len(lst)-1):
            if lst[i] == lst[i+1]:
                acc.append(lst[i])
    return acc

#print(find_duplicates([2,4,4,1,2]))

"""
The worst case run time of find_duplicates(lst)
is O(n) because it uses a for loop at O(n) and sort
at O(n) with multiple uses of append running at O(n),
the overall worst case stands at O(n)
"""
