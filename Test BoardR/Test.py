class ItemStatus:
    OPEN = 'Open'
    TODO = 'Todo'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'
    VERIFIED = 'Verified'

    @classmethod
    def next(cls, current):
        status = [cls.OPEN, cls.TODO, cls.IN_PROGRESS, cls.DONE, cls.VERIFIED]
        index = status.index(current)
        next_index = index + 1 if 0 <= index < len(status) - 1 else len(status) - 1
        return status[next_index]

    @classmethod
    def previous(cls, current):
        status = [cls.OPEN, cls.TODO, cls.IN_PROGRESS, cls.DONE, cls.VERIFIED]
        index = status.index(current)
        prev_index = index - 1 if index > 0 else 0
        return status[prev_index]


next1 = ItemStatus.next(ItemStatus.OPEN)                # Todo
next2 = ItemStatus.next(ItemStatus.TODO)                # In progress
next3 = ItemStatus.next(ItemStatus.IN_PROGRESS)         # Done
next4 = ItemStatus.next(ItemStatus.DONE)                # Verified
next5 = ItemStatus.next(ItemStatus.VERIFIED)            # Verified
prev1 = ItemStatus.previous(ItemStatus.OPEN)            # Open
prev2 = ItemStatus.previous(ItemStatus.TODO)            # Open
prev3 = ItemStatus.previous(ItemStatus.IN_PROGRESS)     # Todo
prev4 = ItemStatus.previous(ItemStatus.DONE)            # In progress
prev5 = ItemStatus.previous(ItemStatus.VERIFIED)        # Done

print(next1)
print(next2)
print(next3)
print(next4)
print(next5)
print(prev1)
print(prev2)
print(prev3)
print(prev4)
print(prev5)
