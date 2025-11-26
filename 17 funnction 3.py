'''A decorator is a function that takes another function as input and returns a new function
Decorator = shortcut + clean code + reusable logic'''

print("==========================decorators=========================")
def changecase(func):
    def inner(name):
        result=func(name)
        if isinstance(result,str):   #check result is string
          return func(name).upper()
        else:
            return result
    return inner      

def square(f):
    def value (val):
        return f(val)*f(val)
    return value


    
@changecase # =>  my_func=changecase(my_func)  decorator:change function behaviour without changing orignal code
def my_func(name):
    return "Hi ! " + name

@changecase
@square     #=>find=changecase(square(find))
def find(val):
    return  3


print(my_func("Ahtsham"))
print(find(3))


print("=========================lambda function======================")
#oneline function take one expression at one time mostly used with built in function map(),filter(),sort()
x=lambda a,b:a+b
print(x(5,6))

print()
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mytripler(11))

print()

print("=============map()=======")

numbers=[1,2,3,4,5]
double=map(lambda a:a*2,numbers)
print(list(double))
print()

print("==============filter()================")

values=[1,2,3,4,5,6,7]
odd=filter(lambda n:n%2!=0, values)
print(list(odd))#filter() returns a filter object, not a list directly. You need to convert it to a list using list().
print()

print("===================sorting===============")
sorting=sorted(values,key= lambda a:-a)#decending
print(sorting)



