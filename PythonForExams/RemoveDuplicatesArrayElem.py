import array as arr

def fun(ar):
    return sorted(set(ar),key=ar.index)

arr1 = arr.array('i',[12,23,43,23,45,12])
print('Original array:')
for i in range(len(arr1)):
    print(arr1[i])

result = arr.array('i',fun(arr1))
print('After removind duplicates:')
for i in range(len(result)):
    print(result[i])
