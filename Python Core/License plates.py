str_letters = input().split(",")

num = int(input())

valid_plate = []

for i in range(num):
    plate = input()

    if \
            plate[0] in str_letters and plate[1] in str_letters and plate[2].isdigit() and plate[3].isdigit() and plate[
                4].isdigit() and plate[5].isdigit() and plate[6] in str_letters and plate[7] in str_letters:
        valid_plate.append(plate)

print(*valid_plate, sep="\n")
