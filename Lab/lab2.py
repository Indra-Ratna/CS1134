#lab 2
#cs 1134
import math
#vitamins

class Poly:
    def __init__(self,lst = [0]):
        self.name = self
        self.lst = lst
        
    def __add__(self,other):
        for i in range(len(self.lst)):
            if(i < len(other.lst)):
                self.lst[i] += other.lst[i]
        if(len(other.lst)>len(self.lst)):
            for i in range(len(self.lst),len(other.lst)):
                self.lst.append(other.lst[i])
        return self.lst
        
            
    def __call__(self,value):
        sum = 0
        for i in range(-1,-len(self.lst)-1,-1):
            sum+=(self.lst[i]*(value**(-i)))
        return(sum)

"""

    

self = [3,7,0,-9,2]
other = [2,0,0,5,0,0,3]

sum = 0
for i in range(-1,-len(self)-1,-1):
    sum+=(self[i]*(1**(-i)))
print (sum)
"""
