n = int(input())
results_lst = []

for i in range(n):
    lines = input().split()
    num_lst = [int(num) for num in lines]
    symmetric = True

    for x in range(len(num_lst)):
        if num_lst[x] != num_lst[-x - 1]:
            symmetric = False
            break

    results_lst.append("Yes" if symmetric else "No")

for result in results_lst:
    print(result)
