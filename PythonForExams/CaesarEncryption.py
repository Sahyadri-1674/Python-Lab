




def caesar_encrypt(text,shift):
    result=''
    for letter in text:
        if letter.isupper():
            shifted = chr((ord(letter) -65 + shift)%26 +65)
        elif letter.islower():
            shifted = chr((ord(letter) -97 + shift)%26 +97)
        else:
            shifted = letter
        result += shifted
    return result

text = input("Enter the input string:")
print(caesar_encrypt(text,2))



def caesar(str,shift):
    res = ''
    shifted=''
    for c in str:
        if c.isupper():
            shifted =  chr((ord(c)-65+shift)+65)
        elif c.islower():
            shifted =  chr((ord(c)-98+shift)+98)
        else:
            shifted = c
        res += shifted
    return res


print(caesar('Prasad',2))
