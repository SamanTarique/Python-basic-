#tuple is a bulit-in data type that used t store data using open brackets()
# tuples items are in ordered at it is unchangable that makes it different
# from list and it also allow duplicate items  tuples itemms are index based 

tuple1=("apple","banana","orange","carrot","banana")
print(tuple1," =>length of tuple1 ",len(tuple1))

print() 
#purpose of comma is to  define the tuple when there is only one element
tuple2=("apple",)# without comma python understand it as a string =>t=("apple")=>type=string
print(type(tuple2)) 

print() 

#tuple()=>constructor is used when we need to convert other iterables into a tuple.like list,set etc
mydict={"a":1,"b":2}
convert=tuple(mydict)#takes only key
print(convert," =>dict convert into tuple") 

takevalue=tuple(mydict.values())
print(takevalue," =>values")

takeitems=tuple(mydict.items())
print(takeitems,"=> items") 

t = tuple(range(5))
print(t)   # (0, 1, 2, 3, 4)


print()

print("==========================access tuple items ===================")
tuple3=("orange","mango","kiwi","leechi")
print(tuple3[1],"# index 1 ") 

print(tuple3[1:3]," => index range from  index 1 to 2 index 3 was not included")
print()
print(tuple3[-4:-1]," => negative indexing")
print()
print(tuple3[0:]," =>print from 0 to end ")
print(tuple3[:3]," =>print from start to 3")
print()

#check item exsist in tuple3
if "orange" in tuple3:
    print("yes orange exsist")
else:
    print("orange doesnot exsist")

print()
print("=======================update tuple=================================")
#“Since a tuple is immutable, we cannot modify it directly. However,
# we can convert the tuple into a list, make the required changes, and then
# convert it back into a tuple.”

# replacing items
tuple4=("saman","khadija","sabiha","amna")
r=list(tuple4)
r[2]="saman"
tuple4=tuple(r)
print(tuple4," =>sabiha replace with saman at index 2")

print()

#appending or adding tuple
tuple5=("aditya","adharsh","aryan","anuj")
y=list(tuple5)
y.append("ahan")
print(tuple(y))

# add tuple to tuple 
tuple6=(1,2,3,4,5)
tuple7=(6,7,8,9)
tuple6 +=tuple7
print(tuple6,"'=> adding two tuple")


# remove element from tuple 
n=list(tuple6)
n.remove(5)
print(tuple(n))
