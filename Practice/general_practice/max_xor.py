class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.value = num

    def find_max_xor(self, num):
        node = self.root
        xor_value = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite_bit = 1 - bit
            if opposite_bit in node.children:
                xor_value = (xor_value << 1) | 1
                node = node.children[opposite_bit]
            else:
                xor_value = (xor_value << 1)
                node = node.children[bit]
        return xor_value


def find_maximum_xor(nums):
    trie = Trie()
    max_xor = 0
    for num in nums:
        trie.insert(num)
    for num in nums:
        max_xor = max(max_xor, trie.find_max_xor(num))
    return max_xor

n = 6
arr = [3, 10, 5, 25, 2, 8]
print(find_maximum_xor(arr))  # 28
