time = input()

h = 0
m = 0
am_pm = 0
if len(time) < 7 or len(time) > 8:
    print("invalid time")

if len(time) == 8:
    h = time[0:2]
    m = time[3:5]
    am_pm = time[6:].upper()

    if time[2] == ":" and time[5] == " " and h .isdigit() and m .isdigit() and (am_pm == "AM" or am_pm == "PM"):
        h = int(h)
        m = int(m)
        if not (1 <= h <= 12 and 0 <= m <= 59):
            print("invalid time")
        elif (h <= 11 and am_pm == "PM") or (h == 12 and am_pm == "AM"):
            print("beer time")
        elif (h == 12 and am_pm == "PM") or (h <= 11 and am_pm == "AM"):
            print("non-beer time")
    else:
        print("invalid time")

if len(time) == 7:
    h = time[0]
    m = time[2:3]
    am_pm = time[5:].upper()

    if time[1] == ":" and time[4] == " " and h .isdigit() and m .isdigit() and am_pm == "AM" or am_pm == "PM":
        h = int(h)
        m = int(m)
        if not (1 <= h <= 12 and 0 <= m <= 59):
            print("invalid time")
        elif (h >= 1 and am_pm == "PM") or (h < 3 and am_pm == "AM"):
            print("beer time")
        elif h >= 3 and am_pm == "AM":
            print("non-beer time")
    else:
        print("invalid time")
