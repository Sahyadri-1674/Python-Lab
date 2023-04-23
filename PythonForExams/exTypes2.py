import types
import matplotlib

code = compile('print("Hello,World")','sample','exec')
print(isinstance(code,types.CodeType))
print(isinstance("print(abs(-111))", types.CodeType))

prasad=types.ModuleType('mymodule')
prasad.study='work hard!'


print(isinstance(matplotlib,types.ModuleType))
print(isinstance(prasad,types.ModuleType))
