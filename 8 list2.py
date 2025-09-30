
# ============remove item in the list we use remove()===================
print()
list1=["apple ","banana","leechi"]
list1.remove("banana")
print(list1,"=> here we remove banana from the list ")

# if we have 2 similar item in alist while using remove method it will the first occurence
list2=["apple ","leechi","banana","leechi"]
list2.remove("leechi")
print(list2,"=> here we remove leechi from the list ")

#we can also use indexes for removing item in the list using pop() method
list2.pop(0)
print(list2,"pop \"apple\" using index")

# also usee del keyword
del list2[1]
print(list2,"remove using del")

#use clear()
list2.clear()
print(list2)

print()
print("==========================Looping using list comprehension================")
# short hand for loop
list3=["apple ","banana","leechi"]
[print(x) for x in list3 ] # it wil print all element of the list

#Write a list comprehension to create a list of squares of odd numbers between 1 and 20.

list4=[x**2 for x in range(1,20) if x%2!=0]
print(list4)

print()
#Create a list comprehension that extracts only the vowels from a string. Example:
s="saman tariq"
list5=[n for n in s if n in 'aeiou']
print (list5)

print()
# write a list comprehnsion that removes all spaces from sencetence
sentence = "Python is fun to learn"
list6=[ n  for n in sentence.split()] # if else as an expression that's why we can write  it before for loop 
print (list6)

print()
# print nested list using list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat=[  num for row in matrix  for num in row] # depend on each other that's why having fix arrangment
print(flat)

print()

# hacker rank question
# x=int(input())
# y=int(input())
# z=int(input())
# n=int(input())
# list1=[ [i,j,k ] for i in range(x+1) for  j in range( y+1)  for  k in range(z+1)  if i+j+k != n ]
# print(list1)

#enumerate() index+value
fruits = ["apple","banana","mango"]

indexed = [(i, fruit) for i, fruit in enumerate(fruits)]
print(indexed)


print()
print("=======================sorting list ======================")

list7=["orange","banana","grapes","apple","cherry"]
list7.sort()
print(list7,"=> print in decending order")

list7.sort(reverse=True)
print(list7," => print in decending order")


list8=[3,8,4,5,2,1,9]
print(list8.sort())
print()

# =========coustomized sorting===================

students = [ ("Sara", 27),("Saman", 19), ("Ali", 22)]#key=>define sorting rules
students.sort(key=lambda x:x[1])# here lambda isa temporary function donot need to give name to function
print(students)# at the basis of age they will sort the list

print()

# Write a Python program that sorts a list of numbers based on their distance from 50.

def myfunc(n):
    return abs(n-50)#abs() that give absolute value  if value is -ve converted into positive always give+answer

list9=[80,40 ,77 ,90,50,100]
list9.sort(key=myfunc)#sort at the basis of myfunc 
print(list9)
print()


list10=[3,6,8,9]
list10.reverse()
print(list10)



