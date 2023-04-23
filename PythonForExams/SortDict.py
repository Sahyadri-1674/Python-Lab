

#my_dict={5:10,3:98,2:0,6:1,9:2,102:4}

#ascending = sorted(my_dict.items(),key=lambda item:item[1])
#print(ascending)
#print(dict(ascending))

#descending= dict(sorted(my_dict.items(),key=lambda item:item[1],reverse=True))
#print(descending)

import operator



my_dict={5:10,3:98,2:0,6:1,9:2,102:4}

ascending = sorted(my_dict.items(),key=operator.itemgetter(1))
print(ascending)
print(dict(ascending))

descending= dict(sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True))
print(descending)
