#question 5
def fibs(n):
    curr,a,b = 0,0,1
    yield b
    while(curr<n-1):
        temp = a+b
        yield a+b
        a = b
        b = temp
        curr+=1 
