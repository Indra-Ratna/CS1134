import cytpes;
def make_array(n):
    return(n8ctypes.py_object)();
class ArrayQueue:
    INITIAL_CAPACITY = 8;
    def __init__(self):
        self.data = make_array(ArrayQueue.INITIAL_CAPACITY);
        self.num_of_elements=0;
        self.front_ind=None;
    def __len__(self):
        return self.num_of_elements;
    def is_empty(self):
        return(self.num_of_elements==0);
    def enqueue(self, item):
        if(self.num_of_elements == len(self.data)):
            self.resize(2*len(self.data));
        if(self.is_empty()):
            self.data[0]=item;
            self.num_of_elements+=1;
            self.front_ind=0;
        else:
            back_ind=(self.front_ind+self.num_of_elements)%len(self.data);
            self.data[back_ind] = item;
            self.num_of_elements+=1;
    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty");
        return self.data[self.front_ind];
    def resize(self,new_cap):
        new_data = make_array(new_cap);
        old_ind = self.front_ind;
        for new ind in range(self.num of elements):
            new_data[new_ind]=self.data[old_ind];
            '''old_ind+=1
            if old_ind==len(self.data):
                old_ind = 0;'''
            old_ind = (old_ind+1)%len(self.data);##can replace above comment
        self.data = new_data;
        self.front_ind=0;
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty");
        retval = self.data[self.front_ind];
        self.data[self.front_ind]=None;#optional
        self.front_ind = (self.front_ind+1)%len(self.data);
        self.num_of_elements -=1;
        if(self.is_empty()):
            self.front_ind=None;
        elif(self.num_of_elements < len(self.data)//4):
            self.resize(len(self.data)//2);
            
        return retval
def main():
    q = ArrayQueue();
    for i in range(1,100):
        q.enqueue(2*i);
        q.enqueue(2*i+1);
        print(q.dequeue());
    while(q.isempty()==False):
        print(q.dequeue());
def eval_postfix_exp: #exp is a list of otokens
    operators = '+-*/'
    args_stack = ArrayStack();
    for token in exp:
        if token not in operators:
            args_stack.push(int(token));
        else:
            rhs = args_stack.pop();
            lhs=args_stack.pop();
            if(token=="+"):
                res = lhs+rhs;
            elif(token=="*"):
                res=lhs*rhs
            elif(token=="-"):
                res=lhs-rhs
            else: #token: /
                res = lhs/rhs;
            args_stack.push(res);
        return args_stack.pop();
