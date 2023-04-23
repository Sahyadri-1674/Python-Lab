import collections

def count_characters(text):

    d=collections.defaultdict(int)
    for char in text:
        d[char] += 1
    print(d.get)
    for item in sorted(d,key=d.get,reverse=True):
        if d[item]>1:
            print('%s %d' %(item , d[item]))

count_characters('thequickbrownfoxjumpsoverthelazydog')

import operator

def count_repeated_letters(text):
   count = {}

   for letter in text:
       if letter in count:
           count[letter] += 1
       else:
           count[letter] = 1
   return count



char_count=count_repeated_letters('thequickbrownfoxjumpsoverthelazydog')
char_count = sorted(char_count.items(),key=operator.itemgetter(1),reverse=True)
for item,val in enumerate(char_count):
  
    if val[1]>1:
        print(char_count[item])
