import requests
api_key = "2ff3614a8b5084cec34ba1d3afdc1225"
parameters = {
    "lat": 52.520008,
    "lon": 13.404954,
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
    print("Bring an umbrella.")
else:
    print("Don't bring an umbrella.")
