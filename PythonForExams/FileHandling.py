import string

from shutil import copyfile
copyfile('test.txt','words2.txt')

def count_words(path):
    with open(path) as f:
        data=f.read()
        data.replace(',',' ')
        
        return len(data.split(' '))

print(count_words('test.txt'))
import string
def letters_file_line(n):
     with open('words2.txt','w') as f:
         alphabets = string.ascii_uppercase
         letters=[alphabets[i:i+n]+'\n' for i in range(0,len(alphabets),n)]
         f.writelines(letters)
letters_file_line(3)
