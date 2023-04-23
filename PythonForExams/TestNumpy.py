import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])
result=np.outer(a,b)
print(result)

c = np.array([[1,2,3],[4,5,6],[7,8,9]])
dia_sum = np.trace(c)
print(dia_sum)

d = np.array([[1,2],[3,4]])
ans = np.linalg.det(d)
print(ans)

e = np.arange(1,10).reshape(3,3)
print(np.linalg.norm(e,'fro'))
print(np.linalg.cond(e,'fro'))


f = np.arange(12,38)

f = f[::-1]
print(f)

g = np.ones((3,3))
g = np.zeros((8,8),dtype=int)
g[1::2,::2]=1
g[::2,1::2]=1
print(g)

l1 = [12,23,34,45,56]
print(np.asarray(l1))
t = ([1,2,3],[4,5,6])
print(np.asarray(t))


def fahrenheit_to_celsius(temp):
    return np.round(((temp - 32)*(5/9)),2)
def celsius_to_fahrenheit(temp):
    return np.round(((temp*(9/5))+32),2)

print(fahrenheit_to_celsius(80),"°C")
print(celsius_to_fahrenheit(-34.44),"°F")

y = np.zeros((5,5))
y += np.arange(5)
print(y)
