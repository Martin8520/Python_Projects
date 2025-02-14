from decimal import Decimal, getcontext


total_value = Decimal('21000000')
min_unit = Decimal('0.21')
min_percent = Decimal('0.000001')

country_vals = [
    Decimal('102841.73844'),
    Decimal('89007.08769'),
    Decimal('23386.85032'),
    Decimal('21251.03225'),
    Decimal('11204.63289'),
    Decimal('2396.84896'),
    Decimal('1579.951601'),
    Decimal('1430.46396'),
    Decimal('1125.1297'),
    Decimal('1124.16072'),
    Decimal('998.90181'),
    Decimal('996'),
    Decimal('952.69898'),
    Decimal('515.99877'),
    Decimal('506.12488'),
    Decimal('197.9'),
    Decimal('196.57845'),
    Decimal('98.15949'),
    Decimal('85'),
    Decimal('81'),
    Decimal('33.84342'),
    Decimal('12'),
    Decimal('9.96325'),
    Decimal('5.99883'),
    Decimal('4.99904'),
    Decimal('4'),
    Decimal('4'),
    Decimal('3.99974'),
    Decimal('2'),
    Decimal('2'),
    Decimal('2'),
    Decimal('2'),
    Decimal('2'),
    Decimal('2'),
    Decimal('2'),
    Decimal('2'),
    Decimal('2'),
    Decimal('1.99962'),
    Decimal('1.99943'),
    Decimal('1.99941'),
    Decimal('0.25399')
]

percentages = []
for value in country_vals:
    full_units = value / min_unit
    percentage = full_units * min_percent
    percentages.append(percentage)

country_total_percentage = sum(percentages)
server_leftover = Decimal('100.000000') - country_total_percentage
total_combined = country_total_percentage + server_leftover

print("Calculated percentages for each country:")
for idx, percentage in enumerate(percentages):
    print(f"{percentage:.15f}%")

print(f"\nTotal Percentage held by countries: {country_total_percentage:.15f}%")
print(f"Server Leftover: {server_leftover:.15f}%")
print(f"Server total: {total_combined:.6f}%")
