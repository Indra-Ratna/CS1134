#question 3
def sums_n (n):
    return sum([i**2 for i in range(n)])
    
    
def sums_n_odd(n):
    return sum([i**2 for i in range(n) if i%2!=0])
