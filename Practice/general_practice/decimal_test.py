from decimal import Decimal, getcontext

getcontext().prec = 28

total_value = Decimal('21000000')
min_unit = Decimal('0.21')
unit_percent = Decimal('0.000001')

country_vals = [
    Decimal('99839'), Decimal('74748'), Decimal('23351'), Decimal('21251'),
    Decimal('11203'), Decimal('1568'), Decimal('1376'), Decimal('1034'),
    Decimal('999'), Decimal('996'), Decimal('514'), Decimal('398'),
    Decimal('203'), Decimal('197'), Decimal('146'), Decimal('81'),
    Decimal('34'), Decimal('12'), Decimal('6'), Decimal('5'),
    Decimal('4'), Decimal('4'), Decimal('2'), Decimal('2'),
    Decimal('2'), Decimal('2'), Decimal('2'), Decimal('2'),
    Decimal('2'), Decimal('2'), Decimal('0'), Decimal('0.000042'),
    Decimal('0.420000'), Decimal('0.210000'), Decimal('0.105000'), Decimal('0.000003')
]

percentages = []
for value in country_vals:
    full_units = value / min_unit
    percentage = full_units * unit_percent
    percentages.append(percentage)

country_total_percentage = sum(percentages)
server_leftover = Decimal('100.000000') - country_total_percentage
total_combined = country_total_percentage + server_leftover

print("Calculated percentages for each country:")
for idx, percentage in enumerate(percentages):
    print(f"County {idx + 1}: {percentage:.12f}%")

print(f"\nTotal Percentage held by countries: {country_total_percentage:.10f}%")
print(f"Server Leftover: {server_leftover:.10f}%")
print(f"Server total: {total_combined:.10f}%")
