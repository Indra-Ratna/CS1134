#lec 5
#2/20/19

"""
-using len(lst) is runtime n because variable
-trying to make constant for runtime

-start of obj = start of array + (index * size of one element

-append is an n runtime operation

ls = []
for i in range(n):
    ls.append(n)
-^ is an n^2 runtime

-when u do something at n for each element
then each element will take 1/n and the
whole thing is n
 -amortized it is theta(1) because constant
"""
import cytpes;

def make_array(n):
    #helper function
    return (n*ctypes.py_object)();
    #make an array of n py_objects

class ArrayList:
    def __init__(self):
        self.data=make_array(1);
        self.capacity=1;
        self.n=0;
    def __len__(self):
        return self.n;
    def append(self,val):
        if (self.n == self.capacity):
            self.resize(2*self.capacity);
        self.data[self.n] = val;
        self.n += 1;

    def resize(self, new_size):
        new_array = make_array(new_size);
        for i in range(self.n):
            new_array[i]=self.data[i];
        self.data = new_array;
        self.capacity = new_size;
        
    def __getitem__(self,ind):
        if (not(0<=ind<=self.n-1)):
            raise IndexError('invalid index');
        return self.data[ind];
    def __setitem__(self,ind,val):
        if (not(0<=ind<=self.n-1)):
            raise IndexError('invalid index');
        self.data[ind:val];

    def __iter__(self):
        for i in range(len(self)):
            yield self[i];
    def extend(self,other):
        #big theta(other.n) in actual analysis not amortized
        if(self.capacity<(self.n+other.n)):
            self.resize(self.n+other.n);
        for elem in other:
            self.append(elem);
    def find_index_of_min(ls):
        min_index = 0;
        for i in range(start+1,len(ls)):
            if ls[i]<ls[min_index]:
                min_index=i;
        return i;
    def selection_sort(ls):
        #big theta(n^2)
        for i in range(len(ls)):
            min_index = find_index_of_min(ls,i);
            temp = ls[i];
            ls[i] = ls[min_index];
            ls[min_index]=temp
    def bubblesort(ls):
        for i in range(len(ls)-1,0,-1):
            for j in range(i):
                if ls[j]>ls[j+1]:
                    temp = ls[j];
                    ls[j]=ls[j+1];
                    ls[j+1]=temp;
    def shortBubbleSort(ls):
        exchanges = True;
        passnum = len(ls)-1
        while passnum>0 and exchanges:
            exchanges = False;
            for i in range(passnum):
            if(ls[i]>ls[i+1]:
               exchange = True;
               temp = ls[i];
               ls[i]=ls[i+1];
               ls[i+1]=temp;
            passnum = passnum-1
