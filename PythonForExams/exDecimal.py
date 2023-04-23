import decimal

num1 = 3.14159
num1 = decimal.Decimal(num1)
print(num1)
print(num1.as_tuple())

str1="123.25"
str1=decimal.Decimal(str1)
print(str1)
print(str1.as_tuple())
