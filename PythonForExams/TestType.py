import types
import decimal
import tkinter as tk
class C:
    def x():
        pass
    def y():
        pass

def p():
    pass

var = C()

print(isinstance(var.x,types.MethodType))
print(isinstance(var.y,types.MethodType))
print(isinstance(p,types.MethodType))


code = compile("print('Hello,World')",'hello.py','exec')
print(isinstance(code,types.CodeType))

print(isinstance(decimal,types.ModuleType))


