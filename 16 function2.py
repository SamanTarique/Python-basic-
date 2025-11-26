# Aribitary positional Argument=*args : (*)=>fixed tell about ulimited number of arguments can enter 
#args= varible name you can write name like *something,*values etc
#unlimited number enter as a tuple

print("==============================*args=============================== ")
def values(rollno,*marks):
    print(" Rollno : ",rollno, " marks = ",marks[2])
    
values(4,96,98,97) # YOU CAN USE LOOP INSIDE THE FUNCTION TO CALLL ALL ELEMENTS 

print()

print("======max num======")
def maxvalue(*numbers):
    if len(numbers)==0:
        return None
    max_value=numbers[0]
    for i in range (len(numbers)):
        if numbers[i]>max_value:
            max_value=numbers[i]
        
            
    return max_value

marks= (38,39,40,33)#must n tuple bcz we are using *args
print(maxvalue(*marks) )     

print()
print("========================**kwargs=====================================")
#Arbitary  keyword argumen :it will take both key and value as an argument
def key_value(student,**info):
    print(f"Student {student} ,department = {info["depart"]}, Section = {info["section"]} ")
    for i ,k in info.items():
        print(i ," : ",k)
    
key_value("Rohan",depart="Artifical_intelligence", section="4A")

print()


print("=============================GloabalScope====,======localScope==============")

x=10
def val():
    c=11
    print("Global_varible + Local_Varable = ", x+c)
    
val()

print()
print("=========================LEGB-Rule===================")
# nested function
# l=local , E=enclosing , G=Global ,B=built-in

def outer():
    x=20 #enclosing
    def inner():
        nonlocal x #used for updating the value of outer variable
        x=28
    inner()    
    print(x)# 28
        
outer()

print("==========================(Function as an argument)=========================")

def calculate(f):
    print(f(5))
    
def square(x):
    return x*x

calculate(square)