#lab 6
def sum_to(n):
    """
    : n type: int
    : return type: int
    """
    if(n<=1):
        return n
    else:
        return n + sum_to(n-1)

def product_evens(n):
    """
    : n type: int
    : return type: int
    """
    if (n==2):
        return n
    else:
        return n*product_evens(n-2)

def find_max(lst,low,high):
    def find(lst,left,right):
        temp = lst[left]
        while(left<right):
            if(lst[left]>=lst[right] and lst[left]>temp):
                temp = lst[left]
                left+=1
            elif(lst[right]>temp):
                temp = lst[right]
                right-=1
            return temp
    return(find(lst,0,len(lst)))
   
def binary_search(lst,val,low,high):
    if high>=1:
        mid = 1+(high-1)/2
        if lst[int(mid)]==val:
            return mid
        elif lst[int(mid)]>high:
            return binary_search(lst,low,mid-1,val)
        else:
            return binary_search(lst,mid+1,high,val)
    else:
        return -1

def is_palindrome(input_str,low,high):
    list(input_str)
    while(low<=high):
        if(input_str[low]==input_str[high]):
            low+=1
            high-=1
            is_palindrome(input_str,low,high)
        else:
            return False
    return True

        
