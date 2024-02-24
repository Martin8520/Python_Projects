import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()

dob = dt.datetime(year=1994, month=3, day=20, hour=23)
print(dob)