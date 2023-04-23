
def not_poor(str):
    snot=str.find('not')
    spoor=str.find('poor')

    if spoor>snot and snot>0 and spoor>0:
        str = str.replace(str[snot:(spoor+4)],'good')
        return str
    else:
        return str

print(not_poor('The lyrics is not that poor!'))  # Output: 'The lyrics is good!'
print(not_poor('The lyrics is poor!'))  
print(not_poor('This sentence does not contain the word poor.'))


cstring=input('Enter comma separated sequence of words:')
words = [word for word in cstring.split(',')]
sorted_cstring = sorted(list(set(words)))
print(','.join(sorted_cstring))


