def is_symmetric(lst):
    length = len(lst)
    for i in range(length // 2):
        if lst[i] != lst[length - 1 - i]:
            return "No"
    return "Yes"


def main():
    N = int(input())

    symmetry_check = []

    for i in range(N):
        numbers = list(map(int, input().split()))
        result = is_symmetric(numbers)
        symmetry_check.append(result)

    for result in symmetry_check:
        print(result)


main()
