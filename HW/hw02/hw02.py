#hw 02

#problem 3
import math
def factors(num):
    acc = []
    for i in range(1,round(math.sqrt(num))+1):
        if (i%num==0):
            acc.append(i)
            yield i
    for i in acc:
        acc.append(num/i)
        yield num/i



def factor(num):
    acc= []
    for i in range(1,round(math.sqrt(num))+1):
        if(num%i==0):
            yield i
            acc.append(i)
    end = len(acc)-1
    for i in range(end,-1,-1):
        if(acc[i]!=(num/acc[i])):
            yield(int(num/acc[i]))
for curr_factor in factor(100):
           print(curr_factor)
