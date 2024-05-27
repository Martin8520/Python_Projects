class SegmentTree:
    def __init__(self, data):
        n = len(data)
        self.n = n
        self.tree = [0] * (2 * n)
        for i in range(n):
            self.tree[n + i] = data[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = min(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, left, right):
        result = float('inf')
        left += self.n
        right += self.n
        while left < right:
            if left % 2:
                result = min(result, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                result = min(result, self.tree[right])
            left //= 2
            right //= 2
        return result


n, q = 5, 5
data = [1, 5, 2, 4, 3]
queries = [
    (2, 1, 5),
    (2, 1, 3),
    (1, 3, 6),
    (2, 1, 5),
    (2, 3, 5)
]

segment_tree = SegmentTree(data)

for query in queries:
    if query[0] == 1:
        _, x, y = query
        segment_tree.update(x - 1, y)
    elif query[0] == 2:
        _, l, r = query
        print(segment_tree.query(l - 1, r))
