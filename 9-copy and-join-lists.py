print("==========================copy list================")

list1=[4,5,6,7,3]
double=list1.copy()# use copy () to copy list 
print(double,"=> here we use copy()")

# we can also use list() to copy a list 
list2=[9,8,8,3,1]
another=list(list2)
print(list2,"=> copy with the help of list function")

#we can also use [:] to copy any list item
list3=list2[:]
print(list3,"=> copy list 2 into list 3")

print()
print("====================join list======================")
list4=list2+list3 #orignal list will not be changed
print(list4)

print()
list2.append(list3)# whole list 3  will count as a elemnt in list2 after appending
print(list2,"=> append() used here")
print(len(list2)," =>  length")

print()
list4.extend(list3)# here every element have its own index also list3 elemnt not like append
print(list4," => extend() used")
print(len(list4),"=>length list4")
