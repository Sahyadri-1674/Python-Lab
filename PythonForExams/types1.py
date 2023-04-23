import types

class C:
    def x():
        return 1
    def y():
        return 1
def is_method(obj):
    return is_instance(obj,types.MethodType)

myobj = C()
print(is_method(myobj.x))
