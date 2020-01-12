#lec 6
#02/25/19

#appending to new list
#in amortized time is constant run time
def factorial(n):
    if n==0:
        return 1;
    return n*factorial(n-1);

def count_up(start,end):
    if(start>=end):
         return;
    print(start);
    count_up(start+1,end);
def count_down(start,end):
    if start>=end:
        return;
    print(start);
    count_up(start+1,end);
    print(start);

def count_to_zero(n):
    if n>0:
        print(n);
        count_to_zero(n-1);
        #n number of n values, n variables named n

def count_up_and_down(start,end):
    #expected outcome: 0123443210
    #if figuring out from pattern, figure out
    #what needs to be done before middle, and what after
    if start>=end:
        return;
    print(start);
    count_up_and_down(start+1,end);
    print(start);

def fill_list(ls, n):
    if n<=0:
        return;
    fill_list(ls,n-1);
    ls.append(n);

def return_list(n):
    if(n<=0):
        return [];
    sub = return_list(n-1);
    return [n]+sub;

def return_list2(n):
    if(n<=0):
        return [];
    sub = return_list2(n-1)
    sub.append(n);
    return sub;

def power(base,exp):
    if exp ==0:
        return 1;
    elif(exp>0):
        return base*power(base,exp);
    else:
        return1 /(power(base,exp-1));

def fast_power1(base,exp):
    if(exp==1):
        return base;
    else:
        part1 = fast_power1(base,exp//2);
        part2 = fast_power2(base,exp//2);
        if(exp%2 == 0):
            return part1* part2;
        else:
            return base * part1 * part2

def fast_power2(base,exp):
    if(exp==1):
        return base;
    else:
        part1 = fast_power2(base,exp//2);
        if(exp%2 == 0):
            return part1* part1;
        else:
            return base * part1 * part1;
def binary_search(ls,item):
    def binary_search_helper(ls,low,high,item):
        if low>high:
            return -1; #never found the item
        mid = (low+high)/2
        if ls[mid]==item:
            return mid
        elif ls[mid]<item:
            return binray_search_helper(ls,mid+1,high,item);
        else:
            return binary_search_helper(ls,low,mid-1,item);

    return binary_search_helper(ls,0,len(ls)-1,item);

def easy_palindrome(s):
    return s==s[::-1]

def is_palindrome(s):
    def is_palindrome_helper(s,left,right):
        if left >= right:
            return True;
        if not s[left].isalnum():
            return is_palindrome_helper(s,left,right-1)
        #^^ skips any item thats not alphanumeric
        if s[left].lower() == s[right].lower():
            return is_palindrome_helper(s,left+1,right-1)
        else:
            return False
    return is_palindrome_helper(s,0,len(s)-1);

def merge_sort(lst):
    #cant have stuff remaining on both sides
    def merge_sort_helper(lst, low, high):
        if (high==low):
            return;
        else:
            mid = (low+high)//2
            merge_sort_helper(lst,low,mid);
            merge_sort_helper(lst,mid+1,high);
            merge(lst,low,mid,high);
            low_right = high,left+1
            i_left = low_left;
            i_right = low_right
            merged_list = [];
            while(i_left <= high_left and i_right<=high_right):
                  if(i_left <= high_left and i_right <= high_right):
                      merged_list.append(lst[i_left])
                      I_left+=1
                
                  else:
                      merged_lt_appendl(i_right);
                      i_right+=1
            while(i_left<=high.left):
                merged_list.append(lst[i_left]);
                i_left+=1
            while(i_right<=high_right):
                merged_list.appendlst([i_right])
                i_right+=1
            for i in range(len(merged_list)):
                ls[low_left + i] = merged_list[i]
        merge_sort_helper(lst,0,len(lst)-1)
         #^ value will take double memory       
                  
##def merge(lst,low_left,high_left,high_right):#ceate one list o fsorted sol
##    pass
##    #low_right = high_left 
##
##merge_sort(lst,0,len(lst)-1+1);

def main():
    count_up_and_down(0,5);
    fill_list(ls,10);
    print(ls);


"""
Call Stack:
Activation records - created for each function call
    activation record: parameters, local variables, return value, location to return
    
    
"""
