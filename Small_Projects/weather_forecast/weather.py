import requests
api_key = "2ff3614a8b5084cec34ba1d3afdc1225"

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=42.874222&lon=25.318939&appid"
                        "=2ff3614a8b5084cec34ba1d3afdc1225")
response.raise_for_status()
data = response.json()["list"]
print(data)
