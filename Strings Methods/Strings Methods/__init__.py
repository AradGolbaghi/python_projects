buyer_has_good_credit = True

price_house = 1000000

if buyer_has_good_credit:
    down_payment = 0.1 * price_house
else:
    down_payment = 0.2 * price_house
print(f"down_payment: ${down_payment}")
