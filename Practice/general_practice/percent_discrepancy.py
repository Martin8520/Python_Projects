from decimal import Decimal

percentages = [
    Decimal('0.475422'), Decimal('0.355944'), Decimal('0.111195'), Decimal('0.101195'),
    Decimal('0.053346'), Decimal('0.007467'), Decimal('0.006552'), Decimal('0.004924'),
    Decimal('0.004757'), Decimal('0.004743'), Decimal('0.002448'), Decimal('0.001894'),
    Decimal('0.000967'), Decimal('0.000936'), Decimal('0.000694'), Decimal('0.000386'),
    Decimal('0.000161'), Decimal('0.000057'), Decimal('0.000029'), Decimal('0.000024'),
    Decimal('0.000019'), Decimal('0.000019'), Decimal('0.000010'), Decimal('0.000010'),
    Decimal('0.000010'), Decimal('0.000010'), Decimal('0.000010'), Decimal('0.000010'),
    Decimal('0.000010'), Decimal('0.000010'), Decimal('0.000001'), Decimal('0.000313')
]

server_leftover = Decimal('98.866746')

total_percentage = sum(percentages) + server_leftover

expected_total = Decimal('100.000000')
discrepancy = total_percentage - expected_total

print(f"Calculated Total Percentage: {total_percentage}")
print(f"Expected Total Percentage: {expected_total}")
print(f"Discrepancy: {discrepancy}")

if discrepancy > 0:
    percentages[-1] -= discrepancy
elif discrepancy < 0:
    percentages[-1] += abs(discrepancy)


adjusted_total = sum(percentages) + server_leftover
print(f"Adjusted Total: {adjusted_total}")
print("Adjusted Percentages:")
for idx, percentage in enumerate(percentages):
    print(f"Player {idx + 1}: {percentage}")
