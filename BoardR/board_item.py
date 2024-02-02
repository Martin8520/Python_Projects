from datetime import date, timedelta

from item_status import ItemStatus, EventLog


def add_days_to_now(d):
    if isinstance(d, date):
        return d
    return date.today() + timedelta(days=int(str(d)))


class BoardItem:
    def __init__(self, title: str, due_date: date, initial_status: str = ItemStatus.OPEN):
        self._title = title
        self._due_date = max(add_days_to_now(due_date), date.today())
        self._status = initial_status
        self._event_logs = [
            EventLog(f"Task created: {self.title}, [{self.status} | {self.due_date.strftime('%Y-%m-%d')}]")]

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if 5 <= len(value) <= 30:
            previous_value = self.title
            self._title = value
            self._event_logs.append(EventLog(f"Title changed from {previous_value} to {self.title}"))
        else:
            raise ValueError("Illegal title length [5:30]")

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        if value >= date.today():
            previous_value = self.due_date
            self._due_date = value
            self._event_logs.append(EventLog(f"DueDate changed from {previous_value} to {self.due_date}"))
        else:
            raise ValueError("New due date must not be in the past")

    @property
    def status(self):
        return self._status

    def revert_status(self):
        previous_status = self.status
        new_status = ItemStatus.previous(self.status)
        if new_status != self.status:
            self._status = new_status
            self._event_logs.append(EventLog(f"Status changed from {previous_status} to {self.status}"))
        else:
            self._event_logs.append(EventLog(f"Cant change status, already at {self.status}"))

    def advance_status(self):
        previous_status = self.status
        new_status = ItemStatus.next(self.status)
        if new_status != self.status:
            self._status = new_status
            self._event_logs.append(EventLog(f"Status changed from {previous_status} to {self.status}"))
        else:
            self._event_logs.append(EventLog(f"Cant change status, already at {self.status}"))

    def history(self):
        return "\n".join([log.info() for log in self._event_logs])

    def info(self, status=None):
        status = status or self.status
        return f"{self.title}, [{status} | {self.due_date.strftime('%Y-%m-%d')}]"


class Task(BoardItem):
    def __init__(self, title, assignee, due_date):
        super().__init__(title, due_date, initial_status=ItemStatus.TODO)
        self._assignee = None
        self._is_initial_assignee = True
        self.assignee = assignee

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        if not value or not (5 <= len(value) <= 30):
            raise ValueError("Assignee must not be empty and its length should be between 5 and 30 characters.")
        if value != self._assignee:
            if not self._is_initial_assignee:
                self._event_logs.append(EventLog(
                    f"Assignee changed from {self._assignee if hasattr(self, '_assignee') else 'None'} to {value}"))
            self._assignee = value
            self._is_initial_assignee = False

    def advance_status(self):
        if self._status != ItemStatus.DONE:
            previous_status = self._status
            new_status = ItemStatus.next(self._status)
            if new_status != self._status:
                self._status = new_status
                self._event_logs.append(EventLog(f"Status changed from {previous_status} to {self._status}"))
            else:
                self._event_logs.append(EventLog(f"Cant change status, already at {self._status}"))

    def history(self):
        base_history = super().history()
        if self._event_logs:
            assignee_change_log = self._event_logs[-1]
            if assignee_change_log.description.startswith("Assignee changed") and \
                    assignee_change_log.description.endswith(self._assignee):
                return base_history
        return f"{self._event_logs[-1].info()}\n{base_history}"

    def info(self, status=None):
        board_item_info = super().info(status=status)
        return f"Task (assigned to: {self.assignee}) {board_item_info}"


class Issue(BoardItem):
    def __init__(self, title, description, due_date):
        super().__init__(title, due_date, initial_status=ItemStatus.OPEN)
        self._description = description if description else "No description"

    @property
    def description(self):
        return self._description

    def advance_status(self):
        if self._status != ItemStatus.DONE:
            previous_status = self._status
            new_status = ItemStatus.next(self._status)
            if new_status != self._status:
                self._status = new_status
                self._event_logs.append(EventLog(f"Status changed from {previous_status} to {self._status}"))
            else:
                self._event_logs.append(EventLog(f"Cant change status, already at {self._status}"))

    def history(self):
        base_history = super().history()
        return base_history

    def info(self, status=None):
        board_item_info = super().info(status=status)
        return f"Issue ({self.description}) {board_item_info}"
