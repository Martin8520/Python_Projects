import random
import smtplib
import datetime as dt
my_email = "martin.b8520@gmail.com"
password = "sznc wall usfr tuef"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n{quote}")

# my_email = "martin.b8520@gmail.com"
# password = "sznc wall usfr tuef"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="antnikbog@gmail.com",
#         msg="Subject:Hello\n\nBody of email. TEST 1 2 3")
