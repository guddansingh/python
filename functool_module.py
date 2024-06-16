import functools
import time

@functools.lru_cache(maxsize=None)
def fun(x):
    time.sleep(5)
    return x*x
    time.sl
    return x*x
    time.sleep(10)
    return x*x

print(fun(2))
print("done the calculation within 5 seconds")
print(fun(5))
print("done the calculation within 7 seconds")
print(fun(10))
print("done the calculation within 10 seconds")

#from this part of print it will not take much time as it given 
# coz we have already given the same vlaues above and using the cache function and those were got memorized 
print(fun(2))
print("done the calculation within 5 seconds")
print(fun(5))
print("done the calculation within 7 seconds")
print(fun(10))
print("done the calculation within 10 seconds")