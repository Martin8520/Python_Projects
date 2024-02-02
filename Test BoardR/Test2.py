from datetime import date, timedelta
from BoardR import item_status


def add_days_to_now(d):
    if isinstance(d, date):
        return d
    return date.today() + timedelta(days=int(str(d)))


class BoardItem:
    def __init__(self, title, due_date):
        if not isinstance(title, str) or not 5 <= len(title) <= 30:
            title = "Invalid title."
            print(title)

        self.title = title
        self.due_date = max(add_days_to_now(due_date), date.today())
        self.status = item_status.ItemStatus.OPEN

    def revert_status(self):
        self.status = item_status.ItemStatus.previous(self.status)

    def advance_status(self):
        self.status = item_status.ItemStatus.next(self.status)

    def info(self):
        return f"{self.title}, [{self.status} | {self.due_date}]"


item = BoardItem('abc', add_days_to_now(-25))
print(item.status)
item.advance_status()
print(item.info())
