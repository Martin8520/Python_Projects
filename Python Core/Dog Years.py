hy = int(input())

if hy <= 2:
    dy = hy * 10
    print(dy)
if hy > 2:
    hy_rem = hy - 2
    dy = (hy - hy_rem) * 10
    hy_to_dy = hy_rem * 4
    print(hy_to_dy + dy)

