import copy

nums_x = [1,2,[3,4],8]
nums_y = copy.copy(nums_x)

print('Original list:',nums_x)
print('Shallow Copy of list:',nums_y)

print('Modifying the shallow copy of the list')
nums_x[0]=10
nums_y[2][1]=5
nums_y[0]=100
print('Original list:',nums_x)
print('Shallow copy after modifications:',nums_y)
