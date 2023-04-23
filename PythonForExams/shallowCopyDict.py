import copy

nums = {'a':2,'b':5,'cc':{'c':8}}
cnums = copy.copy(nums)

print('Original dictionary:',nums)
print('shallow copy of the dictionary:',cnums)
print('Modifying the original dictionary:')
nums['cc']['c']=10
print(nums)
print(cnums)



