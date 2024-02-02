class Board:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item in self.items:
            raise ValueError("Item already in the list")
        else:
            self.items.append(item)

    @property
    def count(self):
        return len(self.items)
