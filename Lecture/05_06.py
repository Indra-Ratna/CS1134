#<5/6/19> Lecture

#Priority Queue ADT
"""
Data Model: a collection of priority-value pairs, that come out in an increasing priorities orer

Operations:

Unsorted Linked List- Min:theta(1) Insert:theta(1) Delete Min:theta(n) Build: theta(n)
Sorted Linked List- Min:theta(1) Insert:theta(n) Delete Min:theta(1) Build: theta(nlog(n))
Balanced Search Tree- Min:theta(1) Insert:theta(log(n)) Delete Min:theta(log(n)) Build: theta(nlog(n))
Heap- Min:theta(1) Insert:theta(log(n)) Delete Min: theta(n)

Heap
-In a heap the minimum value is the root node, left vs right doesn't matter
Def: Let T be a binary tree. We say that T is a Heap if it satisfies:
    1.Heap Order Property: In every node n of T, the priority in n is <= the priorities of n's children
    2.Nearly-Complete Property: If h is the height of T, then all levels:
    0,1,2,...,h-1 have the maximum number of nodes possible, and the remaining nodes, at
    level h, reside in the leftmost possible positions
"""

class ArrayMinHeap:
    class Item:
        def __init__(self,priority, value=None):
            self.priority = priority;
            self.value = value;
        def __lt__(self, other):
            return self.priority < other.priority;
    def __init__(self,priorities_lst = None, values_lst = None):
        self.data = [None];
        #later, I'll add priorities_lst capabilities
    def __len__(self):
        return len(self.data);
    def is_empty(self):
        return len(self)==0;

    def min(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty!");
        item = self.data[1]
        return (item.priority, item.value);
    def swap(self, a, b):
        self.data[b],self.data[a] = self.data[a],self.data[b];
    def fix_up(self, location):
        if (location ==1):
            return; #no need to swap anywhere, it's correct!
        else:
            parent = location//2;
            if(self.data[location]<self.data[parent]):
                #self.data[location],self.data[parent]=self.data[parent],self.data[location]
                self.swap(location,parent);
                self.fix_up(parent);#recurse if needed
            #else: Don't need b/c there is nothing to do
    def delete_min(self):
        if self.is_empty():
            raise Exception("Priority Queue is Empty");
        self.swap(1,len(self.data)-1); #swqap the root and the last nodes
        item = self.data.pop();
        if(self.is_empty()):
            self.fix_down(1); #maintain the heap property
        return (item.priority, item.value);

    def has_left(self, location):
        return location*2 <= len(self.data)-1;
    def has_right(self,location):
        return(location*2+1) <= len(self.data)-1;
    def fix_down(self, location):
        if(self.has_left(location)):
            left = location*2;
            if (self.has_right(location)):
                #has both left and right
                right = location*2+1
                if (self.data[right] < self.data[left]):
                    small_child = right;
            if(self.data[small_child] < self.data[location]):
                self.dwap(location, small_child);
                self.fix_down(small_child);
    def insert(self,priority, value = None):
        self.data.append(ArrayMinHeap.Item(priority, value));
        self.fix_up(len(self.data)-1);

