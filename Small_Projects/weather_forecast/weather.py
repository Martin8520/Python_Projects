import requests
from twilio.rest import Client

account_sid = "ACb04042299677b98d6fd36b6c39eeb53d"
auth_token = "7e94ebb707d67726001b67189f4db0f0"


api_key = "2ff3614a8b5084cec34ba1d3afdc1225"
parameters = {
    "lat": 40.712776,
    "lon": -74.005974,
    "appid": api_key,
    "cnt": 12
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=42.874222&lon=25.318939&appid"
                        "=2ff3614a8b5084cec34ba1d3afdc1225", params=parameters)

response.raise_for_status()
data = response.json()
weather = data["list"][0]["weather"][0]["id"]
will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is raining in New York",
        from_="+15855801816",
        to="+359889257027"
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is not raining in New York.",
        from_="+15855801816",
        to="+359889257027"
    )
    print(message.status)