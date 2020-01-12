#lec 2(/3)
#02/04/2019
"""
Iterators:
for var in iterable-collection:
    ---------------
    ---------------
Iterable-collection : an object that produces an iterator

lst = [1,2,3]
lst_iter = iter(lst)
lst_iter2 = iter(lst)
next(lst_iter)->1
next(lst_iter)->2
next(lst_iter2)->1***
next(lst_iter)->3
next(lst_iter)->error

s = "abc"
s_iter = iter(s)
next(s_iter)->a
next(s_iter)->b
next(s_iter)->c
next(s_iter)->error

-Simulating a for loop-
ex:
s = 'abc'
s_iter = iter(s)
end = False
while(end == False):
    try:
        item = next(s_iter)
        print(item)
    except StopIteration:
        end = True

-Simulating the range function-
ex: poor efficiency->
for elem in my_range(3,10,0.5):
    print(elem)
def my_range(start,stop,step):
    res = []
    curr = start
    while(curr<stop):
        res.append(curr)
        curr += step
    return res

-Generator-
def f():
    x=1
    yield x
    x+=1
    yield x
    x+=1
    yield x
>>>g = f()
-g is generator object-
>>>next(g)
1
>>>next(g)
2

#generator is iterator that allows code to break execution
when yield is reached[ snapshot fo active data frame taken
and stored] or next is called[ data that was saved is
restored and execution resumes where left off]#

def my)range(start,stop,step):
    curr = start
    while(curr<stop):
        yield curr
        curr+=step


-Asymptotic Analysis-
Primality test->
def: :let num>=2 be an int. We say that num is prime,
if its only divisors are 1 and num
    Examples:
    13 is prime       12 is not prime

For optimal speed only check from 1 to root num, then find
other factors using complimentary divisors.
    -if num is 100 then check for (1,2,4,5,10) then complete with
    (20,25,50,100)

-We find the asymptotic order of the number of primitive operations
executed by a process as a function of its input size
"""
import math

def factors(num):
    for curr in range(1,num+1):
        if num%curr == 0:
            yield curr;
for factor in factors(99):
    print(factor);

def is_prime1(num):
    count_divs = 0;
    for curr in range(1,num+1):
        if(num%curr==0):
            count_divs+=1
    if(count_divs==2):
        return True;
    else:
        return False;
def is_prime2(num):
    count_divs = 0;
    for curr in range(1,int(math.sqrt(num))+1):
        if(num%curr==0):
            count_divs+=1
    if(count_divs==2):
        return True;
    else:
        return False;
    
