def count_moves(start, arr, instructions):
    arr = list(map(int, arr.split(',')))
    forward_sum = 0
    back_sum = 0

    for order in instructions:
        steps, direction, size = order.split()
        steps = int(steps)
        size = int(size)

        if direction == 'forward':
            for i in range(steps):
                start = (start + size) % len(arr)
                forward_sum += arr[start]
        elif direction == 'backwards':
            for i in range(steps):
                start = (start - size) % len(arr)
                back_sum += arr[start]

    return forward_sum, back_sum


start_position = int(input())
array_string = input()
move_instructions = []

while True:
    instruction = input()
    if instruction == 'exit':
        break
    move_instructions.append(instruction)

forward_result, backward_result = count_moves(start_position, array_string, move_instructions)

print(f"Forward: {forward_result}")
print(f"Backwards: {backward_result}")
