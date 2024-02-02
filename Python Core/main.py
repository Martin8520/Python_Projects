lines = int(input())

min_vowel_ratio = float("inf")
best_food = None
best_v = 0
best_letters = 0

for i in range(lines):
    food = input()

    total_v = 0
    total_letters = 0

    for char in food:
        if char.isalpha():
            total_letters += 1
            if char in "aeiou":
                total_v += 1

    if total_letters > 0:
        v_ratio = total_v / total_letters
    else:
        v_ratio = 0

    if v_ratio < min_vowel_ratio or (v_ratio == min_vowel_ratio and total_v > best_v) or (v_ratio == min_vowel_ratio and total_v == best_v and total_letters > best_letters):
        min_vowel_ratio = v_ratio
        best_food = food
        best_v = total_v
        best_letters = total_letters

print(f"{best_food} {best_v}/{best_letters}")

