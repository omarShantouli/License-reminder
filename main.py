import smtplib
import datetime
my_email = "samigogo339@gmail.com"
password = "samigogo1990"

if datetime.datetime.now() == datetime.datetime(2026, 10, 8):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="hantoli797@gmail.com",
            msg="Subject:License Reminder"
                "\n\n Your License will be expire after a week from now"
        )


elif datetime.datetime.now() >= datetime.datetime(2026, 10, 15):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="hantoli797@gmail.com",
            msg="Subject:License Reminder"
                "\n\n Your License is expired "
        )