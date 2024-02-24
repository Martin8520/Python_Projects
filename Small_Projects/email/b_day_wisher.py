import smtplib

my_email = "martin.b8520@gmail.com"
password = "sznc wall usfr tuef"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="antnikbog@gmail.com",
        msg="Subject:Hello\n\nBody of email. TEST 1 2 3")
