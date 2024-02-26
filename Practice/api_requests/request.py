import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()["iss_position"]["longitude"]
data2 = response.json()["iss_position"]["latitude"]
iss_position = (data, data2)
print(iss_position)
