class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue(6)
queue.enqueue(8)
queue.enqueue(13)
queue.enqueue(14)
queue.enqueue(15)
print(queue.size())
