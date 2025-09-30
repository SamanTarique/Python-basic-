 #list items are  ordered(while adding an item move to ward right(rightshifting)) changable and 
 # allow duplicte list items are index based index start from '0'
 
list1=["apple","banana","leechi","kiwi"]
print(list1[1],"=> 1")
print()

list2=("Female",24,True,"male",6)
l2=list(list2)#here we use list()=>constructor(that return new object) to converted list2 into list
print(l2,"=>2")
print(len(l2),"=>length")#list length
print(type(l2))#check type

print()
#------------------range  of index,negative indexing--------------------------
list3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list3[2:7],"=>Indexing")#it will make a new list from cherry to melon
print(list3[:4])
print(list3[-4:-1],"=>negative indexing")#negindex start from -1(mango) 


print()
#------------check element in list-------------
if "blueberry" in list3:
    print("yes blueberry is in list")
else:
    print("not present=>check list")

#-------------------Replacing through index-------------
list4=["apple","banana","cherry","orange", "kiwi", "melon"]
list4[1]=["icecream"]
print(list4," => here we replace banana with icream")

print()
print()

            #===========Replacing list in Range=============
list4[2:4]=["watermelon","blueberry"]
print(list4," = replacing in range from 2:4")#4th was not included

"if you give less range and add greater num of item in list then next wil move toward right side "

list4[1:2]=["Potato","tomato","Garlic"]
print(list4," = item moves toward right")

print()
print()

"if you provide greater range and adding less value it will left the place of another item"
print(list4)
print(len(list4),"=>length  of list 4 before add less value")
print()
list4[3:5]=["carrort"]
print(list4,"=> left space")
print(len(list4),"=>length of list 4 after add less value")

print()
print()
print()
#--------using insert() work without replacing it will add the item innside the list-----------------
list5=["book","pencil","clipboard"]
list5.insert(2,"sunscream")
print(list5)

print()
print()
"using append() that wll add a element or a list in the end of list that will count as a element "
list5.append("selfsih")
print(list5,"here we use append")
print(len(list5),"see length")
print()
print()

"using extend it will add a list as an seperate item that will also count as their length"
list6=["cocunut","leechi","Potato"]
list5.extend(list6)
print(list5,"here we use extend")
print(len(list5))