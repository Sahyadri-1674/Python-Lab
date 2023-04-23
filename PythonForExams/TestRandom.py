import random
import string

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
hex_col = "#{:02x}{:02x}{:02x}".format(r,g,b)
print(hex_col)

print(random.randint(5,20))
print(random.randint(100,110))
print(random.randint(-10,10))

print(random.randint(1,10)*7)


rstring=''
maxi=255

for i in range(random.randint(1,maxi)):
    rstring += random.choice(string.ascii_letters)

print(rstring)


print(random.random())

random.seed('123')
random_int=random.randint(1,10)
print(random_int)


population = range(0,100)

num_list = random.sample(population,10)
print(num_list)
no_of_elements = 4

mul_items = random.sample(num_list,no_of_elements)
print(mul_items)
