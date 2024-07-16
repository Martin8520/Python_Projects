from collections import deque


def countStudents(students, sandwiches):
    students_queue = deque(students)
    sandwiches_stack = sandwiches

    while students_queue:
        if students_queue[0] == sandwiches_stack[0]:
            students_queue.popleft()
            sandwiches_stack.pop(0)
        else:
            students_queue.append(students_queue.popleft())

            if students_queue.count(students_queue[0]) == len(students_queue):
                break

    return len(students_queue)


print(countStudents([1, 1, 0, 0], [0, 1, 0, 1]))  # 0
print(countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))  # 3
