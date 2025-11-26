# Function: is a block of code ,that is used to avoid  code repetation ,
# start with a lettr or underscore ,return result ,provide  an output(use def keyword),you can call it any time

print("=================Function============")
def greet(): 
    print("Hi! welcome in python world")
    
greet()#call function


print("===============Function with multiple parameter===============")
def adding(a,b):#adding name of function , a,b:parameter that pass any value(argument)
    return (a+b)

n=adding(5,6)#=>call function (5,6=>argument)
print(n,"=>Result")

print()
print("===================Function with default parameter===========")

def intro(name="Saman"):
    print("hello",name)
    
intro("Ahan")

print()
print("===================passing any argument ==============")
# you can send any data type as an argument to  function

def my_function(person):
    for i ,j in person.items():
       print(i,":",j) 
    print("name:",person["name"])
    
my_person={"name":"Ahtsham","age":20}
my_function(my_person)
   
print("================== return different data type=============")
# like: list,tuple, dictionary, set, string, number, bool or any multiple values
def values():
    return ["apple","banana","kiwi","cherry"]

print(values())

print("==================positional argument====,keyword argument===========")

def student(name,subject):
    print(f" Student name = {name} , Subject = {subject} ")
  
print() 

student("Aliana","Maths")   #directly gives name  
print("Alina and Maths both are => positional argument ")  

print()

student(subject="Science",name="Anush")# order was not same with function parameter but the value is fixedl ike  name have anush 
print("name=Anush,Subject=Science lke key have value  are => keyword arguments")



