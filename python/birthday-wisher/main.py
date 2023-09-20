import pandas
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")

# Creating dictionary in the following format:
# {(month, day): name, email, year, month, day}
# To loop through DataFrame iterrows() method is used:
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthdays.iterrows()}

# Creating tuple of today's date
today = (dt.datetime.now().month, dt.datetime.now().day)

MY_EMAIL = "GMAIL_ADDRESS_HERE"
MY_PASSWORD = "GMAIL_APP_PASSWORD_HERE"

# 2. Check if today matches a birthday in the birthdays.csv
if today in birthday_dict:
    person = birthday_dict[today]["name"]
    person_email = birthday_dict[today]["email"]

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
    # actual name from birthdays.csv
    random_letter = f"./letter_templates/{random.choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])}"
    with open(random_letter) as letter:
        SUBJECT = f"Happy Birthday {person}!"
        MESSAGE = letter.read().replace("[NAME]", person)

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Turning on the mail encryption
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person_email,
            msg=f"Subject: {SUBJECT}\n\n{MESSAGE}",
            mail_options=()
        )
