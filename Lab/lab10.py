#lab 10

#problem 1
def sum_dll(dll):
    """
    do recursively
    """
    if dll.is_empty():
        raise Exception
    first= dll.first_node()
    return sum_dll_helper(first,dll)

def sum_dll_helper(first)
    if first.next is dll.trailer:
        return first.data
    return sum_dll_helper(first.next,dll)+first.data

#problem 2
def reverse_dll_by_data(dll):
    first = header.next
    while first.next is not trailer:
        temp = first.next
        first.next = temp.next
        temp.next.prev = first
        temp.next = first
        temp.prev = header
        first.prev = temp
        header.next = temp

def reverse_dll_by_node(dll):
    first = dll.first_node()

#problem 3
class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        ###
    def __len__(self):
        '''Returns the number elements in the stack.'''
    def is_empty(self):
        '''Returns true if stack is empty and false otherwise'''
    def push(self, e):
        '''Adds an element, e, to the top of the stack.'''
    def top(self):
        '''Returns the element at the top of the stack.
            An exception is raised if the stack is empty.'''
    def pop(self):
        '''Removes and returns the element at the top of the
            stack. An exception raised if stack is empty'''
    def mid_push(self, e):
        '''Adds an element, e, to the middle of the stack. An
            exception is raised if the stack is empty.'''

#problem 4
def n_bonacci(n, k):
    '''
    : n, k type: int
    : yield type: int
    '''
    def helper_n_bonacci(n, k):
        if n
