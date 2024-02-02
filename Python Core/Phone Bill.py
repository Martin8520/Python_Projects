text_total = int(input())
calls_total = int(input())

free_calls = 60
free_text = 20
base_fee = 12.00
add_price_text = 0.06
add_price_calls = 0.10
sales_tax = 0.20

extra_text = text_total - free_text if text_total > free_text else 0
extra_calls = calls_total - free_calls if calls_total > free_calls else 0

total_price = (extra_calls * add_price_calls) + (extra_text * add_price_text)

tax = 0

if extra_text > 0 or extra_calls > 0:
    tax = total_price * sales_tax

bill_total = base_fee + total_price + tax

if extra_text > 0:
    print(f"{extra_text} additional messages for {extra_text * add_price_text:.2f} levas")
else:
    print(f"0 additional messages for 0.00 levas")

if extra_calls > 0:
    print(f"{extra_calls} additional minutes for {extra_calls * add_price_calls:.2f} levas")
else:
    print(f"0 additional minutes for 0.00 levas")

if tax > 0:
    print(f"{tax:.2f} additional taxes")
else:
    print("0.00 additional taxes")

if bill_total > base_fee:
    print(f"{bill_total:.2f} total bill")
else:
    print(f"{base_fee:.2f} total bill")
