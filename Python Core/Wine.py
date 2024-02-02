colleagues = int(input())
vineyard_len = int(input())
vineyard_x = input()
perfect_quality_grapes = 0
average_quality_grapes = 0
for i in range(vineyard_len):
    if vineyard_x[i] == "X":
        perfect_quality_grapes = perfect_quality_grapes + 7
    elif vineyard_x[i] == "x":
        average_quality_grapes = average_quality_grapes + 7
glasses_wine = perfect_quality_grapes * 5
glasses_rakia = (average_quality_grapes // 5) * 14
difference_wine = glasses_wine - colleagues * 2
difference_rakia = glasses_rakia - colleagues
if difference_wine < 0:
    if abs(difference_wine) % 5 != 0:
        bottles_wine = (abs(difference_wine) // 5) + 1
    else:
        bottles_wine = abs(difference_wine) // 5
else:
    bottles_wine = difference_wine // 5
if difference_rakia < 0:
    if abs(difference_rakia) % 14 != 0:
        bottles_rakia = (abs(difference_rakia) // 14) + 1
    else:
        bottles_rakia = abs(difference_rakia) // 14
else:
    bottles_rakia = difference_rakia // 14
if difference_wine < 0 and difference_rakia < 0:
    print(f"No! {bottles_wine} more bottles of wine and {bottles_rakia} more bottles of rakia required!")

elif difference_wine < 0 <= difference_rakia:
    print(f"No! {bottles_wine} more bottles of wine and 0 more bottles of rakia required!")
elif difference_wine >= 0 > difference_rakia:
    print(f"No! 0 more bottles of wine and {bottles_rakia} more bottles of rakia required!")
elif difference_wine >= 0 and difference_rakia >= 0:
    print(f"Yes! {bottles_wine} bottles of wine and {bottles_rakia} bottles of rakia remaining for the next party!")
