total_value = 21000000.0
min_unit = 0.21
min_percent = 0.000001

country_vals = [
    99838.57339, 74848.32839, 23352.85032, 21251.03225, 11202.63289, 2393.84896,
    1568.078521, 1375.85749, 1344.12244, 1031.76516, 998.91255, 996, 513.99877,
    196.57845, 145.81806, 81, 33.84342, 12, 5.99911, 4.99904, 3.99965, 3.99883,
    2, 2, 2, 2, 2, 1.99962, 1.99943, 1.99941, 0.25399
]

percentages = []
for value in country_vals:
    full_units = value / min_unit
    percentage = full_units * min_percent
    percentages.append(percentage)

country_total_percentage = sum(percentages)
server_leftover = 100.0 - country_total_percentage
total_combined = country_total_percentage + server_leftover

print("Calculated percentages for each country:")
for idx, percentage in enumerate(percentages):
    print(f"{percentage:.6f}%")

print(f"\nTotal Percentage held by countries: {country_total_percentage:.6f}%")
print(f"Server Leftover: {server_leftover:.6f}%")
print(f"Server total: {total_combined:.6f}%")
