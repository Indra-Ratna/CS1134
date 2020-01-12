#Indra Ratna
#Question 2
#HW 3

import ctypes

def make_array(n):
    return (n*ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def insert(self, index, val):
        if(index<0 or index>len(self)):
            raise IndexError("ArrayList index out of range")
        else:
            self.extend(val)
            for i in range(len(self),index-1,-1):
                self[i] = self[i-1]
            self[index] = val

    def __len__(self):
        return self.n

    def pop(self,index=len(self)-1):
        if(len(self)<1):
            raise IndexError
        temp = self[index]
        self[index] = None
        return temp

    def __repr__(self):
        return ("["+",".join([str(i) for i in self]) + "]")
    
    def __add__(self,other):
        ls3 = ArrayList()
        ls3 += self
        ls3 += other
        return ls3

    def __iadd__(self,other):
        for i in range(other.n):
            self.append(other[i])
        return self

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_size

    def __getitem__(self, ind):
        if not (abs(ind) <= len(self)-1):
            raise IndexError("ArrayList index is out of range.")
        elif ind < 0:
            ind = len(self) + ind
        return self.data[ind]

    def __setitem__(self, ind, val):
        if not (abs(ind) <= len(self) - 1):
            raise IndexError("ArrayList index is out of range")
        elif ind < 0:
            ind = len(self) + ind
        self.data[ind] = val

    def __mul__(self,scalar):
        newlst = ArrayList()
        for i in range(scalar):
            for x in range(len(self)):
                newlst.append(self[x])
        return newlst

    def __rmul__(self,other):
        return self*scalar

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]

    def extend(self, other_iterable):
        for elem in other_iterable:
            self.append(elem)
