

def hashify(str):
    str_list = str.split()
    
    j=0
    for word in str_list:
        hashes=''
        if len(word)>=5:
            l=len(word)
            for i in range(l):
                hashes += "#"
            str_list[j]=hashes
        j+=1
    str=' '.join(str_list)
    return str

str = "Count the lowercase letters in the said list of words:"
newstr= hashify(str)
print(newstr)
