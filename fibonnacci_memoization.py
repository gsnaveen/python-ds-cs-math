
from collections import defaultdict
import sys

sys.setrecursionlimit(10**8)

def febcached():

    cache = defaultdict(int)

    def feb(n):
        valcache = cache.get(n,None)
        if valcache:
            # print("Cache hit",n)
            return valcache
        elif n < 2 :
            val = n
        else:
            val = feb(n-1) + feb(n - 2)

        cache[n] = val

        return val

    return feb

myFeb = febcached()

print(myFeb(100))
