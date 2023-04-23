from decimal import Decimal
import decimal


pi = 3.1429
pidec = Decimal(pi)
print(pidec)
print(pidec.as_tuple())

strf = '123.25'
strdec = decimal.Decimal(strf)
print(strdec)
print(strdec.as_tuple())


def round_to_10_cents(x):
    remainder = x.remainder_near(Decimal('0.10'))
    if abs(remainder)== Decimal('0.05'):
        return x
    else :
        return x - remainder
for n in range(80,120):
    y = Decimal(n)/Decimal('1E2')
    print('{0} roundes to {1}'.format(y,round_to_10_cents(y)))
