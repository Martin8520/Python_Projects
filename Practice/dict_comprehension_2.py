weather_c = eval(input())
# 🚨 Don't change code above 👆
weather_f = {day: (temp * 9/5 + 32) for (day, temp) in weather_c.items()}

# Write your code 👇 below:


print(weather_f)