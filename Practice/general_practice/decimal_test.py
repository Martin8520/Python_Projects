from decimal import Decimal, getcontext



total_value = Decimal('21000000')
min_unit = Decimal('0.21')
min_percent = Decimal('0.000001')

country_vals = [
    Decimal('99838.57339'),
    Decimal('74848.32839'),
    Decimal('23352.85032'),
    Decimal('21251.03225'),
    Decimal('11202.63289'),
    Decimal('2393.84896'),
    Decimal('1568.078521'),
    Decimal('1375.85749'),
    Decimal('1344.12244'),
    Decimal('1031.76516'),
    Decimal('998.91255'),
    Decimal('996'),
    Decimal('513.99877'),
    Decimal('196.57845'),
    Decimal('145.81806'),
    Decimal('81'),
    Decimal('33.84342'),
    Decimal('12'),
    Decimal('5.99911'),
    Decimal('4.99904'),
    Decimal('3.99965'),
    Decimal('3.99883'),
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
    print(f"{percentage:.6f}%")

print(f"\nTotal Percentage held by countries: {country_total_percentage:.6f}%")
print(f"Server Leftover: {server_leftover:.6f}%")
print(f"Server total: {total_combined:.6f}%")
