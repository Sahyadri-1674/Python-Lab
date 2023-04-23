
class py_solution():
    def int_to_Roman(self,num):
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        i=0
        roman=''
        while num>0:
            div=num//val[i]
            while div:
                roman += sym[i]
                num -= val[i]
                div -= 1
            i+=1
        return roman

num = int(input("Enter num:"))
print("Roman numerals of",num,"is:",py_solution().int_to_Roman(num))


class BracketValidator:
    def __init__(self,s):
        self.stack = []
        self.s = s
    def is_valid(self):
        for c in self.s:
            if c in ['(','{','[']:
                self.stack.append(c)
            
            elif c in [')','}',']']:
                if not self.stack:
                    return False
                prev = self.stack.pop()
                if (c==')' and prev!='(') or (c=='}' and prev!='{') or (c==']' and prev!='['):
                    return False
        return not self.stack
                

brackets = input('Enter a string:')
validate = BracketValidator(brackets)
if validate.is_valid():
    print('String is valid')
else :
    print('String is not valid')
    
