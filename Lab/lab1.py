#cs 1134
#lab 1 coding
import random
from random import shuffle

#problem 1
def add_binary(bin_num1, bin_num2):
    """
    bin_num1 - type: str
    bin_num2 - type: str
    return value - type: str
    """
    b = bin_num1
    b2 = bin_num2
    lst1 = [int(b[i])*(2**i) for i in range (len(b))]
    s1 = sum(lst1)
    lst2 = [int(b2[i])*(2**i) for i in range (len(b2))]
    s2 = sum(lst2)
    sums = s1+s2
    print(sums)

#problem 2
def can_construct(word, letters):
    """
    word - type: str
    letters - type: str
    return value - type: bool
    """
    l = list(letters)
    
    for char in word:
        if char in l:
            del(l[l.index(char)])
        else:
            return False
    return True

#problem 3
def create_permutation(n):
    lst = [i for i in range (n)]
    shuffle(lst)
    return(lst)

def scramble_word(word,space):
    lst = list(word)
    c = create_permutation(len(list))
    acc =""
    for i in c:
        acc += lst[i]+space
    return acc

def game(word):
    out = scramble_word("pokemon","  ")
    print("Unscramble the word: ",out)
    i = 1
    while(i<4):
        ty = input("Try #",i,": ")
        if ty == word:
            print("You got it")
            return True
    print("you lost, it was",word)
    return False

    
