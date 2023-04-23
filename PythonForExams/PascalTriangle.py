
def pascal_triangle(n):

    trow=[1]
    y=[0]
    for i in range(max(n,0)):
        print(trow)
        #print(y)
        #print('Passed:',trow+y,y+trow)
        #x=zip(trow+y,y+trow)
        #print(tuple(x))
        trow=[l+r for l,r in zip(trow+y,y+trow)]
        
    return n>=1

pascal_triangle(6)


def fun(n):
    trow=[1]
    y=[0]
    for i in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y,y+trow)]
    return n>=1

def squares():
    sq=[i**2 for i in range(1,21)]
    print(sq)

squares()
