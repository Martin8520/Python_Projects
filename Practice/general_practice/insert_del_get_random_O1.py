import random


class RandomizedSet:

    def __init__(self):
        self.data = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.data.append(val)
        self.val_to_index[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        last_element = self.data[-1]
        index_to_remove = self.val_to_index[val]

        self.data[index_to_remove] = last_element
        self.val_to_index[last_element] = index_to_remove

        self.data.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))  # True
print(randomizedSet.remove(2))  # False
print(randomizedSet.insert(2))  # True
print(randomizedSet.getRandom())  # 2
print(randomizedSet.remove(1))  # True
print(randomizedSet.insert(2))  # False
print(randomizedSet.getRandom())  # 2
