#lab3
#asymptotic analysis

def reverse_list(lst):
    """
    :lst type: list[]
    :return type: None
    """
    for i in range(len(lst)):
        lst.insert(i,(lst.pop()))
    return lst

def reverse_lst(lst):
    for i in range(len(lst)//2):
        holder = lst[len(lst)-1]
        lst[len(lst)-1-i] = lst[i]
        lst[i] = holder

def reverser(lst):
    left = 0
    right = len(lst) -1
    while(left<right):
        lst[left],lst[right] = lst[right],lst[left]
        left+=1
        right+=1

def is_palindromeME(s):
    sent = list(s)
    return sent==reverse_list(sent)


def is_palindromSOL(s):
    l = 0
    r = len(lst)-2
    for i in range(len(lst)//2):
        if lst[1] != lst[r]:
            return False
        l+=1
        r-=1
    return True


def move_zeroes(nums):
    for i in nums:
        if i==0:
            nums.insert(0,i)


def find_missing(lst):
    """
    1a: runtime is O(n^2)
    :nums type: list[int] (sorted)
    :return type: int
    """
    for i in range(len(lst)-1):
        while(lst[i]+1 != lst[i+1]):
            return lst[i]+1
def find_miss(lst):
    if lst[len(lst)//2] == (lst[-1]+lst[0])/2:
        return
        
    
