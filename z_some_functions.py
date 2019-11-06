isdigit()
isalpha()
isalnum()
isinstance(val,dict)
class Foo:
  a = 5
fooInstance = Foo()
print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))

import sys
sys.setrecursionlimit(10**6)


import json
json.loads(dictString) # Converting String into a dictionary
