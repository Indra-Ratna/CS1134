#Indra Ratna
#Question 4
#HW 3

def remove_all(lst, value):
    count = 0
    i = 0
    while i < (len(lst)):
        if lst[i]==value:
            print(i,"index")
            count+=1
            lst += [lst.pop(i)]
        else:
            i+=1
    print(lst)
    for i in range(count):
        lst.pop()
    return lst

list = [1,2,3,3,4]
print(remove_all(list,3))
