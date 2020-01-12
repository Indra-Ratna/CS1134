#lec 9
"""
dynamic arrays:
- pros -
    random access: jump to any position at any given time
    efficiently amortize poerformance for adding/removing at end [sometimes at fast times it maybe inaccurate]
- cons -
    storing data contiguously in the memory is issue with VERY big data set
    insertions/deletions at interior positions are expensive unless at end of array
    amortized bounds may be unacceptable in real time

linked list:
    -every node contains a data element and a pointer to the 'next' node in the list
    -no element
    -doubly linked lists contain both a previous and a next point
"""
class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data;
        self.next = next;
        self.prev = prev;
head = Node();
head.data = 1;
head.prev = None;
head.next = Node();
head.next.data = 2;
head.next.prev = head;
head.next.next = None;

#iterate over the list
##temp = head;
##while (temp is not None):
##    print(temp.data);
##    temp = temp.next;
##print("End of list");
print_list(head);

#add zero onto list
head.prev = Node(0,head);
head = head.prev;

print_list(head);

temp = head;
while temp.next is not None:
    temp = temp.next;
temp.next = Node(4,prev=None,next=temp);

#linked list
class LinekdList:
    class Node:
        def __init__(self,data=None, next = None,prev = None):
            self.data = data;
            self.next = next;
            sself.prev = prev;
        def disconnect(self):
            self.data = None;
            self.next = None;
            self.prev = None;
    def __init__(self):
          self.head = LinkedList.Node();
          self.tail = LinkedList.Node();
          self.head.next = self.tail;
          self.tail.prev = self.head;
          self.size = 0;

    def __len__(self):
        return self.size;

    def is_empty(self):
        return len(self)==0;

    def first_node(self):
        if (self.is_empty()):
            raise Exception("List is empty");
        return self.head.next;

    def last_node(self):
        if(self.is_empty()):
            raise Exception("List is empty");
        return self.tail.prev;

    def add_after(self,node,data):
        new_node = LinkedList.Node(data);
        follower = node.next;
        node.next = new_node;
        new_node.next = follower;
        new_node.prev = node;
        follower.prev = new_node;
        self.size +=1;
        return new_node;
""""
        node.next =node.next.prev = LinkedList.Node(data,next=node.next,prev=node);
        return node.next;
  """  
    def add_first(self,data):
        return self.add_after(self.head,data);
    def add_last(self,data):
        return self.add_after(self.tail.prev,data);
    def delete_node(self, node):
        node.prev.next = node.next;
        node.next.prev = node.prev;
        self.size -=1;
        retval = node.data;
        node.disconnect();
        return retval;
    def delete_first(self):
        if (self.is_empty()):
            raise Exception ("List is empty");
        return self.delete_node(self.first_node());
    def delete_last(self):
        return self.delete_node(self.last_node());
    def __iter__(self):
        if(self.is_empty()):
            return;
        cursor = self.first_node();
        while cursor is not self.tail:
            yield curosr.dta;
            cursor = cursor.next;

    def __repr__(self):
        return "["+"<-->".join([str(item) for item in self]) +"]";
    def clear(self):
        while not self.is_empty():
            self.delete_first();

def remove_value(llist,val):
    if llist.is_empty():
        return;
    cursor = llist.first_node();
    while cursor is not llist.tail:
        if cursor.data == val:
            llist.delete_node(cursor);
            trmp = cursor;
            cursor = cursor.next;
            llist.delete_node(temp);
        else;
            cursor = cursor.next();
11 = LinkedList();
for i in range(10):
    1.add_last(i);
print(1);
