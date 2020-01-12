#lab 4
def str_to_int(int_str):
    total = 0
    for i in int_str:
        total = total*10+int(i)
    return total


def reverse_vowels(input_str):
    ls = list(input_str)
    left = 0
    right = len(ls)-1
    vowel= 'aeiou'
    while(left<right):
        if ls[left] in vowel and ls[right] in vowel:
            ls[left],ls[right]=ls[right],ls[left]
            left+=1
            right-=1
        if(ls[left] not in vowel):
            left+=1
        if(ls[right] not in vowel):
            right-=1
    return ''.join(ls)

    
def jump_search(lst,val,k):
    """
    : lst type: list[int]
    : val, k type: int
    : return type: int (if found), None(if not found)
    """
    index = 0
    while(index<len(lst)):
        if(lst[index] == val):
            print ("curr",lst[index])
            return index
        if(lst[index]<=val):
            print("index",index)
            index += k
        if(lst[index]>val):
            print("third if")
            step = 1
            while(step<k+1):
                if(lst[index-step]==val):
                    print('step',step)
                    return index-step
                step+=1
    return None
jump_search([1,2,3,4,5,6,7,8,9,10],5,2)


def jump(lst,val,k):
    curr = 0
    jump = k
    while(curr_jump < len(lst) and lst[curr]<val):
        curr+=jump
    if(lst[curr]<val):
        curr=len(lst)-1
    for i in range(jump):
        if lst[curr] == val:
            return curr
            curr-=1
    return None

def exponential_search(lst,val):
    """
    : lst type: list[int]
    : val type: int
    : return type: int(if found), None(if not found)
    """
    jump = math.floor(math.sqrt(len(lst)) 
    while(curr_jump < len(lst) and lst[curr]<val):
        curr+=jump
    if(lst[curr]<val):
        curr=len(lst)-1
    for i in range(jump):
        if lst[curr] == val:
            return curr
            curr-=1
    return None
            
