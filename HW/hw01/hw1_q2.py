#question 2
def shift(lst,k,position = "left"):
    move = len(lst)-1
    place = 0
    if(position =="left"):
        move = 0
        place = len(lst)-1
    for i in range(k):
        lst.insert(place,lst.pop(move))
    return lst

#question 3
def sums_n (n):
    return sum([i**2 for i in range(n)])
    
    
def sums_n_odd(n):
    return sum([i**2 for i in range(n) if i%2!=0])

#question 4
lst4A = [(10**i) for i in range(6)]
lst4B = [i+(i**2) for i in range(10)]
lst4C = [chr(i) for i in range(97,123)]


#question 5
def fibs(n):
    curr,a,b = 0,0,1
    yield b
    while(curr<n):
        temp = a+b
        yield a+b
        a = b
        b = temp
        curr+=1        


#question 6
class Vector:
    def __init__(self, d):
        if isinstance(d,int):
            self.coords = [0] * d
        elif isinstance(d,list):
            self.coords = d
    def __len__(self):
        return len(self.coords)
    def __getitem__(self, j):
        return self.coords[j]
    def __setitem__(self,j,val):
        self.coords[j] = val
    def __add__(self,other):
        if(len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self,other):
        return self.coords == other.coords
    def __ne__(self,other):
        return not(self == other)
    def __str__(self):
        return '<'+str(self.coords)[1:-1]+'>'
    def __repr__(self):
        return str(self)
    def __sub__(self,other):
        new = Vector(len(self))
        for i in range(len(self.coords)):
            new[i] = (self[i]-other[i])
        return new
    def __neg__(self):
        new = Vector(len(self))
        for i in range(len(self)):
            new[i] = -1*self[i]
        return new
    def __mul__(self,other):
        if isinstance(other,Vector):
            acc = 0
            for i in range(len(self)):
                acc += (self[i]*other[i])
            return acc
        else:
            new = Vector(len(self))
            for i in range(len(self)):
                new[i] = (self[i]*other)
            return new
    def __rmul__(self,other):
            new = Vector(len(self))
            for i in range(len(self)):
                new[i] = (self[i]*other)
            return new





        
##        if(type(self)==type(val)):
##            sum = 0
##            for i in range(len(self)):
##                sum += self[i] * val[i]
##            return sum
##        elif(isinstance(self,Vector) and isinstance(val,int)):
##            new = Vector(len(self))
##            for i in range(len(self)):
##                new[i]= val*self[i]
##            return new
##        elif(isinstance(self,int) and isinstance(val,Vector)):
##            new = Vector(len(val))
##            for i in range(len(val)):
##                new[i] = self*val[i]
##            return new
        
    
    






                 
