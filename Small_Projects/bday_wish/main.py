import random
from datetime import datetime
import pandas
import smtplib

EMAIL = "martin.b8520@gmail.com"
MY_PASSWORD = "sznc wall usfr tuef"

today = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
