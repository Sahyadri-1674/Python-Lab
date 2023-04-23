
def divide(x,y):
    try:
        div=x/y
        print(f"{x}/{y}={div}")
    except ZeroDivisionError as e:
        print('Exception occured:',e)
    except ValueError as e:
        print('Exception occured:',e)
    except Exception as e:
        print('Error Occured:',e)

a=int(input('Enter num1:'))
b=int(input('Enter num2:'))
divide(a,b)
