import decimal
print('Configuring rounding to round to the floor')
decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_FLOOR
print(decimal.Decimal(20)/decimal.Decimal(6))

print('Configuring rounding to round to the ceil')
decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_CEILING
print(decimal.Decimal(20)/decimal.Decimal(6))

print('Configuring rounding to round to nearest integer')
decimal.getcontext().prec = 1
decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
print(decimal.Decimal(10)/decimal.Decimal(4))
