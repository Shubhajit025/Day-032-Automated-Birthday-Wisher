# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas
import os


# 1. Update the birthdays.csv
now = dt.datetime.now()
date = now.date()
day = date.day
month = date.month
today_tuple = (month, day)


birth_day_info = pandas.read_csv("birthdays.csv")
birthday_list = birth_day_info.month.to_list() + birth_day_info.day.to_list() + birth_day_info.name.to_list() + birth_day_info.email.to_list()
birthday_dict = {(row.month, row.day): row for (index, row) in birth_day_info.iterrows()}


SENDER_EMAIL = os.environ.get("MY_EMAIL")
SENDER_PASS = os.environ.get("MY_PASSWORD")
try:
    RECEIVER_EMAIL = birthday_dict[today_tuple]["email"]
except KeyError:
    print("Coming soon!")
else:
    # 2. Check if today matches a birthday in the birthdays.csv
    if today_tuple in birthday_dict:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter:
            wisher = letter.read()
            new_letter = wisher.replace("[NAME]", birthday_dict[today_tuple]["name"])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASS)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject:Happy Birthday.\n\n{new_letter}"
            )

