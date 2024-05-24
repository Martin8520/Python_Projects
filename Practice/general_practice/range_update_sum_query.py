class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _update_range(self, start, end, l, r, value, node):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2 + 1] += self.lazy[node]
                self.lazy[node * 2 + 2] += self.lazy[node]
            self.lazy[node] = 0

        if start > end or start > r or end < l:
            return

        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * value
            if start != end:
                self.lazy[node * 2 + 1] += value
                self.lazy[node * 2 + 2] += value
            return

        mid = (start + end) // 2
        self._update_range(start, mid, l, r, value, node * 2 + 1)
        self._update_range(mid + 1, end, l, r, value, node * 2 + 2)
        self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

    def update_range(self, l, r, value):
        self._update_range(0, self.n - 1, l, r, value, 0)

    def _query_range(self, start, end, l, r, node):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2 + 1] += self.lazy[node]
                self.lazy[node * 2 + 2] += self.lazy[node]
            self.lazy[node] = 0

        if start > end or start > r or end < l:
            return 0

        if start >= l and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left_query = self._query_range(start, mid, l, r, node * 2 + 1)
        right_query = self._query_range(mid + 1, end, l, r, node * 2 + 2)
        return left_query + right_query

    def query_range(self, l, r):
        return self._query_range(0, self.n - 1, l, r, 0)

    def _build(self, arr, start, end, node):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, start, mid, node * 2 + 1)
            self._build(arr, mid + 1, end, node * 2 + 2)
            self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

    def build(self, arr):
        self._build(arr, 0, self.n - 1, 0)


def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])
    q = int(data[idx + 1])
    idx += 2

    arr = [int(data[i]) for i in range(idx, idx + n)]
    idx += n

    seg_tree = SegmentTree(n)
    seg_tree.build(arr)

    result = []
    while idx < len(data):
        query_type = int(data[idx])
        if query_type == 1:
            l = int(data[idx + 1]) - 1
            r = int(data[idx + 2]) - 1
            v = int(data[idx + 3])
            seg_tree.update_range(l, r, v)
            idx += 4
        elif query_type == 2:
            l = int(data[idx + 1]) - 1
            r = int(data[idx + 2]) - 1
            result.append(seg_tree.query_range(l, r))
            idx += 3

    sys.stdout.write('\n'.join(map(str, result)) + '\n')

