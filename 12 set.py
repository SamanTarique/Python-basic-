'''A set:  is a collection of value stored in a single variable  
   which is unordered, unchangeable*, and unindexed. set donot allow duplicate value 
   set are written with curly bracket => { }'''

#true 1 are consisdered as  a value in set =>it give concept of duplication when wrte in a set

set1={1,2,3,True,"apple"}
print(set1)#     it will show only value=1 not value=true 


#False and 0 also considered as a value 

set2={False,4 ,5 ,7 ,0,9,8,"book"} #also have different type of element in set
print(set2) 
print(type(set2))
print(len(set2),"=> length of set2")

print()
print("==========================access items===================================")
#use for loop or in key word
set1={1,2,3,True,"apple"}
for i in set1:
    print(i)
  
print("=========in=======")    
#using (in) keyword
print(3 in set1)#it will give boolean answer =>true bcz true is present in set 
print("banana" not in set1)    

print()
print("====================================add-items==================================")
set3={2,3,4}
set4={5,6,7,8}
set3.add(1)#using add() to add  1 in set3 (only modify the set doesnot return)
print(set3)
print()
set3.update(set4)# using update for join both set together set3 with set4
print(set3)
# we can also use update() for joining set element with any iterable( list ,dict ,tuple or itself) element


print("====================================remove-items=========================")
#remove():remove the element from the set but if elemnt is not present in the set it will give an error
set4={4,6,8,9}
set4.remove(9)
print(set4,"=<using remove function")
# discard(): it also dicard/remove element but it doesnot give an errr while element is not present in set
set4.discard(5)
print(set4,"=>usingdiscard() ")
print()
# pop()
set5={1,2,3,4,5,6,7}
set5.pop()
print(set5)

#clear():clear all elemnt present in the set and show empty set
set4.clear()
print(set4)
# # del():also remove the existance of the set 
# del set5
# print(set5)give error

print()
print("==========union  ,intersection ,difference ,symmetricdifference =======(return frozenset)======")

'''union:::: combine  two sets elements together OR
 1stset+tuple/union  necessary having set at 1st num'''

set6={6,5,8,9}
tuple1=(1,2,3,3)

set7=set6.union(tuple1)# actual set6 remain same for changing actual set use update()
print(set7,"=>using union()")

a={5,4,8,9,}
b={3,2,1,5,4,8}
print(a|b," => using a|b")# this operator use only for sets both a and b are set
print()

'''intersection()::::: it will show common between two sets necessary having both a and b are sets'''

c=a.intersection(b)# actual a set remains un changed

print(c,"=>intersection()")

print(a&b,"=>using & ")#work same as intersetion()

a.intersection_update(b)# changes a set also
print(a,"=>using intersection_update")



print()
'''difference():::: “The difference between two sets is a new set containing
elements that are in the first set but not in the second.”'''

a.difference(b)
print(a,"=>using difference()")# actual set a element remain unchanged

set8={9,8,7,4}
set9={5,8,9,4,6}

print(set8-set9,"=>using -")# work same as difference()

set8.difference_update(set9)# make changes in actual set 
print(set8)

'''symmetricdfference:::: Symmetric difference: “The symmetric difference between two sets is
# a new set containing all the elements that appear in either set but not in both'''

set8={9,8,7,4}
set9={5,8,9,4,6}

set11=set8.symmetric_difference(set9)
print(set11,"=>using symmetric_difference")

print(set8^set9,"=>using ^")# work same as symmetric diiference

set11.symmetric_difference_update(set9)
print(set11,"=>using symmetric_diifeence_update()")


