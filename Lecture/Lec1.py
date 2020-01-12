#cs 1134
#01/30/19 lec 2
##-Mutating list: indexed assignment(lst[i]=...), append, insert, pop, reverse, sort
##-Constructing new list: list literals([1,2,3],[]), list constructor, +, *, slicing,
##copy.copy, copy.deepcopy
##-Reference(var name) exists in memory map and points to object which reference the
##list which refers to the data. When you increment a data value, it doesn’t change
##it just refers to a new literal
##-Iterators: useful for looping, an iterable-collection is an object that produces
##an iterator via the syntax iter(iterable-collection)



def squares_list(n):
    res = []
    for k in range(1,n+1):
        res.append(k*k);
    return res;

def squares_list2(n):
    return[k*k for k in range(1,n+1)];
    #use square brackets to define it as list

def tens_list(n):
    return [10*k for k in range(1,n+1)];

def tens_list_even(n):
    return [10*k for k in range(1,n+1) if k%2==0];
    #if statement is called a predicate

def make_tuple(s):
    #string s
    return [(i,s[i],ord(s[i])) for i in range (len(s))];
    #returns a tuple of (index, value, unicode)

class Counter:
    def __init__(self):
        self.value = 0;
    def inc(self):
        self.value +=1
    def __repr__(self):
        return str(self.value);

def demo1():
    cl = Counter();
    cl.inc();
    print(cl);
    cl.inc();
    cl.inc();
    print(c1);

    c2 = Count();
    c2.inc();
    print(c2);

def demo2():
    #uses one counter rather than five
    A = [Counter()]*5;
    for c in A:
        c.inc();
        print(c);

def demo3():
    A = [Counter() for i in range(5)];
    for c in A:
        c.inc();
        print(c);
#demo3();



#iterators and generators
def main():
    lst = [1,2,3]
    list_iter1 = iter(lst)
    list_iter2 = iter(lst)
    next(list_iter1) # returns 1
    next(list_iter1) # returns 2
    next(list_iter2) # returns 1
    # they r pointers to different locations
