target_num = int(input())

input_numbers = input().split()
numbers = [int(num) for num in input_numbers]

found_pairs = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_num:
            found_pairs = True
            print(f"{numbers[i]},{numbers[j]}")
if not found_pairs:
    print("no pairs")
