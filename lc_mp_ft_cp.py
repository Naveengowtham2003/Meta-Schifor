#list comprehension
import pandas as pd
lis = [i**2 for i in range(10)]
d= {"Square of numbers":lis}
s = pd.DataFrame(d)
print(s)

#Map Example

def square(x):
    return x**2

mp = list(map(square,range(10)))
print(mp)

#Filter
def is_even(x):
    return x % 2==0

fl = list(filter(is_even,range(10)))
print("Filter Function ", fl)

#Closure
def oufn(x):
    def infn(y):
        return x+y
    return infn
cl = oufn(10)
result  = cl(20)

print("Closure result",result)


