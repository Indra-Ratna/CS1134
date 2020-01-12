#hw 02
#problem 4
import math
def e_approx(n):
    start = 1
    val = 1
    curr = 2
    if n==0:
        return 1
    while(curr<n+1 and n>1):
        val += (1/math.factorial(curr))
        curr+=1
    return val+1


