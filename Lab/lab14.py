#lab 14 q1 ( DoublyLinkedBase)
class PlayList(self):
    def __init__(self):
        self.songs = ChainingHashTableMap()
        self.songs_list = DoublyLinkedList()

    def add_song(self,new_song):
        self.songs_list.add_last(new_song)
        self.songs[new_song] = self.songs_list.last_node()
    def add_song_aft(self,song_name,new_song_name):
        if song_name not in self.songs:
            raise KeyError("song:", song_name,"not found.")
        if self.last == song_name:
            self.add_song(new_song_name)
        else:
            self.songs[new_song_name] = self.songs[song_name]
            self.songs[song_name] =#### 

    def add_song_after(self, song_name, new_song_name):
        #rip this is add_song again
        if self.last is None:
            self.songs[new_song_name] = None
            self.first=new_song_name
        else:
            self.songs[self.last] = new_song
            self.songs[new_song_name] = None

        self.last = new_song_name

    def play_song(self, song_name):
        pass

    def play_list(self):
        pass

    def __repr__(self):
        print("Playing"+self.ls)


def print_tree_level(bin_tree, level):
    queue = ArrayQueue()
    queue.enqueue(bin_tree.root)
    while level > 0:
        length = len(queueu)
        for i in range(length):
            front = queue.dequeue()
            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)
        level -=1
    while not queue.is_empty():
        print(queue.dequeue().data, end= " ")
    print()
print("\nTesting print_tree_level with queueu(BFS):")
for i in range(6):
    print_tree_level(bin_tree, i)


def ptl(root,level):
    if level == 0:
        print(root.data, end = " ")
    else:
        if root.left is not None:
            ptl(root.left, level-1)
        if root.right is not None:
            ptl(root.right, level-1)
print("Testing recursion")
ptl(bin_tree.root,3)
        
                



              



    
    
