from datetime import timedelta

from board_item import Task, add_days_to_now, Issue

issue = Issue('App flow tests?', 'We need to test the flow!', add_days_to_now(1))
task = Task('Dont refactor anything', 'Pesho', add_days_to_now(2))

for board_item in [issue, task]:
    print(board_item.info())
