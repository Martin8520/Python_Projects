from datetime import datetime


class EventLog:
    def __init__(self, description: str):
        if not description:
            raise ValueError("Description cannot be empty.")

        self._description = description
        self._timestamp = datetime.now()

    @property
    def description(self):
        return self._description

    @property
    def timestamp(self):
        return self._timestamp

    def info(self):
        formatted_timestamp = self.timestamp.strftime('%m/%d/%Y, %H:%M:%S')
        return f"[{formatted_timestamp}] {self.description}" if self.timestamp else f"{self.description}"


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
