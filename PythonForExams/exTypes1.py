import types

class C:
    def x():
        return 1
    def y():
        return 1
def is_method(obj):
    return isinstance(obj,types.MethodType)

myobj = C()
print(is_method(myobj.x))
print(is_method(myobj.y))
print(isinstance(is_method,types.MethodType))
