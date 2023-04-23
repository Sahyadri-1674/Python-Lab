import numpy as np

a = np.array([[1,2],[4,5]])

b= np.array([[1,2],[4,5]])

arr= np.array([[1,2,3],[4,5,6],[7,8,9]])
diag_sum = np.trace(arr)
print(diag_sum)

result = np.outer(a,b)
determinant = np.linalg.det(a)
print(determinant)
print(result)

c = np.arange(12,38)
print('Original array:')
print(c)
print('Reverse array:')
c = c[::-1]
print(c)


d = np.arange(1,10).reshape(3,3)
print("Original array:")
print(d)

x = np.linalg.norm(d,'fro')
y = np.linalg.cond(d,'fro')
print(x)
print(y)

z = np.ones((3,3))
z = np.zeros((8,8),dtype=int)
z[1::2,::2]=1
z[::2,1::2]=1
print(z)

list1=[12,23,34,45]
tuple1=([1,2,3],[4,5,6])

print(np.asarray(list1))
print(np.asarray(tuple1))

m = np.zeros((5,5))
print(m)
m += np.arange(5)
print(m)
