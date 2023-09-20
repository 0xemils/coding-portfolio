import smtplib

SUBJECT = "ISS is overhear now!"
MESSAGE = "Hey!\n\nISS is overhead right now. Look up!"


class EmailSender:
    def __init__(self):
        self.my_email = "SENDER_GMAIL_ADDRESS_GOES_HERE"
        self.password = "SENDER_GMAIL_PASSWORD_GOES_HERE"  # It is needed to create an app password in gmail settings

    def send_email(self):
        # By using with statement it is not needed to use connection.close()
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # Turning on the mail encryption
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs="RECIPIENT ADDRESS",
                msg=f"Subject: {SUBJECT}\n\n{MESSAGE}",
                mail_options=()
            )
