 # in python we are also extract the value back into the variables that we called unpacking
print("=====================tuple_update================")
vegetable=("potato","tomato","mashroom")
(brown,red ,yellow)=vegetable
print(brown+" "+red+" "+yellow)

print()
tuple2=("apple"," banana","cherry","strawberry","kiwi","leechi","mango")
(green,yellow,*bloodred,pink)=tuple2
print(green,yellow,bloodred,pink)# use * asteric here :if we have less number variables then
#values we can use asteric to assign remaing values to asteric varble in the form of list 

print()
'''we can also use loop for and while loop to acess the element using (range or in)'''
print("=====================Multiply_tuple================")

fruits = ("apple", "banana", "cherry")
print(fruits * 2)# it will print tuple 2 time we donot use multiply(*)in set and dictionary

print("=====================join_tuple================")
tuple3=vegetable+tuple2
print(tuple3)

print("=====================Method_in_tuple================")
tuple4=(1,2,3,4,2,4,1)
print(tuple4.count(4))# it will count how many time 4 repeat in tuple


#index():tell about specific value position :give the first occurance :if value not found give exception(error)

tuple5 = ["apple", "banana", "cherry", "banana"]
print(tuple5.index("banana"))

#print(tuple5.index("mango"))=>it will give error



