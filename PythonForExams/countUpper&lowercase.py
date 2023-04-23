

def count_case(str):
    d={'Uppercase':0,'Lowercase':0}

    for c in str:
        if c.isupper():
            d['Uppercase'] += 1
        elif c.islower():
            d['Lowercase'] += 1
        else:
            pass
    print('Original String:',str)
    print('Uppercase character count:',d['Uppercase'])
    print('Lowercase character count:',d['Lowercase'])

count_case('The quick Brown Fox')

def is_perfect_number(num):
    sum = 0
    for x in range(1,num):
        if num%x==0:
            sum += x
    return sum==num

print(is_perfect_number(6))
