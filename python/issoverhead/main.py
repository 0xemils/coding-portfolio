import requests
from datetime import datetime, timezone
from config import EmailSender
import time

MY_LAT = 00.789650  # Your latitude
MY_LONG = 00.457186  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def iss_nearby():
    if (MY_LAT-5 < iss_latitude < MY_LAT+5) and (MY_LAT-5 < iss_longitude < MY_LAT+5):
        return True
    else:
        return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc)

    if sunrise >= time_now.hour >= sunset:
        return True
    else:
        return False


email_sender = EmailSender()

while True:
    # If the ISS is close to my current position and it is currently dark
    if iss_nearby() and is_dark():
        # Then email me to tell me to look up.
        email_sender.send_email()
        # Running the code every 60 seconds.
    time.sleep(60)
