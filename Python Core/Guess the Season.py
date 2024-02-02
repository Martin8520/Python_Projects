month = input()
day = int(input())

if month == "March" and day <= 20 or (month == "April" or month == "Mau"):
    print("Spring")
elif month == "June" and day >= 21 or (month == "July" or month == "August") or (month == "September" and day <= 21):
    print("Summer")
elif month == "September" and day >= 22 or (month == "October" or month == "November") or (month == "December" and day <= 20):
    print("Autumn")
else:
    print("Winter")