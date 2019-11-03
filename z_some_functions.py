isdigit()
isalpha()
isinstance(val,dict)
class Foo:
  a = 5
fooInstance = Foo()
print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))

import sys
sys.setrecursionlevel(10**6)
