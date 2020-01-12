#None <= h <==> 60] <==> [50] <==> [10] <==> [20] <==> [30] <==> t => None

def get_itewm*self,i):
    if not self.is_empty():
        if 0 <= i <= len(self)//2: # start from header
            node = self.header.next #first node
            while i >= 0:
                node = node.next #bump the pointer forward
                i -= 1       
            return node.data

        elif len(self)//2 <= i < len(self): #start from trailer
            node = self.trailer.prev# node is not obj just pointer
            while i < len(self)//2:
                node - node.prev
                i -=1
            return node.data

        else: #out of range
            raise IndexError('index out of range')
    else:
        raise Empty("DOubly linked list is empty")
