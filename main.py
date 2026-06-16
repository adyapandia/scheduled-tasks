import os
import smtplib
import random
from datetime import datetime
import pandas

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
mail_content = random.choice(letters_list)

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    with open(f"letter_templates/{mail_content}", "r") as f:
        contents = f.read()
        letter = contents.replace("[NAME]", birthdays_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{letter}"
                            )
