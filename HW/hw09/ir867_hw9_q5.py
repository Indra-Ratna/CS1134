#hw9 q5
from ChainingHashTableMap import ChainingHashTableMap

class InvertedFile:
    def __init__(self, file_name):
        with open(file_name) as file:
            chars = file.read().split()

        self.map = ChainingHashTableMap()
        i = 0
        for item in chars:
            word = item.strip(",?!.'\"").lower()
            self.map[word] = []

        for item in chars:
            word = item.strip(",?!.'\"").lower()
            self.map[word].append(i)
            i += 1

    def indices(self, word):
        lower = word.lower()
        i = self.map.hash_function(lower)

        if self.map.table[i] is not None:
            for item in self.map.table[i]:
                if item == lower:
                    return self.map.table[i][lower]
        return[]
