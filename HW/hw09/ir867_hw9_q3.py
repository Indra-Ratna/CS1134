#hw9 q3
import random
import UnsortedArrayMap

class ChainingHashTableMap:

    def __init__(self, N=64, p=123123123):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p-1)
        self.b = random.randrange(0, self.p-1)

    def hash_function(self,k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self,key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is not None:
            if isinstance(curr_bucket, UnosrtedArrayMap.UnsortedArrayMap.Item):
                return curr_bucket.key
            else:
                return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        if self.table[i] is None:
            self.table[i] = UnosrtedArrayMap.UnsortedArrayMap.Item(key, value)
            self.n+=1
        elif isinstance(self.table[i], UnsortedArrayMap.UnsortedArrayMap):
            old_size = len(self.table[i])
            self.table[i][key] = value
            new_size = len(self.table[i])
            if(new_size > old_size):
                self.n += 1
            if(self.n > self.N):
                self.rehash(2*self.N)
    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        del curr_bucket[key]
        self.n -=1
        if curr_bucket.is_empty():
            self.table[i] = None
        if(self.n < self.N // 4):
            self.rehash(self.N // 2)


    def rehash(self, new_size):
        old = []
        for key in self:
            if isinstance(key, UnosrtedArrayMap.UnsortedArrayMap.Item):
                old.append(key.key, key.value)
            else:
                old.append(key,self[key])
        self.__init__(new_size)
        for(key,val) in old:
            self[key] = val
            
def print_hash_table(ht):
    for i in range(ht.N):
        print(i,": ",sep = "", end = "")
        curr_bucket = ht.table[i]
        if isinstance(curr_bucket, UnosrtedArrayMap.UnosrtedArrayMap.Item):
            print("(", curr_bucket.key,", ",curr_bucket.value,")",sep="",end="")
        elif curr_bucket is None:
            print(end="")
        else:
            for key in curr_bucket:
                print("(", key,", ",curr_bucket[key],")",sep="",end="")
        print()
ht = ChainingHashTableMap()
for i in range(100):
    ht[i*i] = i
print_hash_table(ht)
