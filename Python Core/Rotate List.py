numbers = input().split(',')

n = int(input())

n = n % len(numbers)

rotated_lst = numbers[n:] + numbers[:n]

print(','.join(rotated_lst))
