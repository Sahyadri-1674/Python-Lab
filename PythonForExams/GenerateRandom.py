import random
import string

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

hex_col = "#{:02x}{:02x}{:02x}".format(r,g,b)

print(f'Random color is:{hex_col}')

max=20
random_string=''
for x in range(max):
    random_char = random.choice(string.ascii_letters)
    random_string += random_char
print(random_string)


print(random.randint(3,24))
print(random.randint(-10,10))


print(random.randint(0,10)*7)
