# def:IN DICTIONARY WE Store the elelment in the formof  key and value dict is changable,
# (acc:python 3.7)orderable,also donot allow duplicate values using{key:value}brackets

print("==========get()==========")

dict1={"name":"Saman","Father":"Tariq","Mother":"Shabnam","s_Age":19}
print(dict1.get("Father"))

print("=======================values()==================================")
print(dict1. values())# it will print the values of the key 

print()
print("=============================keys()======================")
print(dict1.keys())# print keys of the values 

print()
print("=========================items()=====================================")
print(dict1.items()) #print key+value whole item


print("==========check==========")
key="s_Age"
if key in dict1:
    print(True)
else:
    print(False)
        
print("==============update======================")
dict1.update({"updating_age":20})  
print(dict1)
print()

print("=====================add item=================================")
dict1["country"]="Pakistan"
print(dict1)

print("==========================update existing value=========================")
dict1.update({"Father":"Tariq Rajput"})
print(dict1)

print()
print("==========================pop()================================")
dict1.pop("updating_age")# delete pecific item 
print(dict1)

print()
print("===============popitem()==========")
dict1.popitem()#delete last inserted item
print(dict1)

print("=======================copy()=================")
dict2=dict1.copy()
#or
dict3=dict(dict1)

print(dict2," =>dict2")
print(dict3," =>dict3")

print("===========clear()============")
dict3.clear()
print(dict3,"=>dict3 ")

# #we can also use del
# del dict2
# print(dict2)#it will give an error

print("===========================loop in dict========================")
#print keys of dict1
for i in dict1:
    print(i)


print()
#print values 
for i in dict1:
    print(dict1[i])
    
    
print()
#print values
for i in dict1.values():
    print(i)
    
print()
#print keys
for i in dict1.keys():
    print(i)
 
print() 
#print whole items  
for i in dict1.items():
    print(i)   

print("============================nested dict1=================")
dict4={
    "Fruits":{
        "Mango":"yellow","apple":"red","kiwi":"brown"
    },
    "Animal":{
        "cat":"meow","dog":"bhao,bhao","goat":"maaaaaaa"
    }
}

print(dict4["Animal"]["dog"])

print()
## loop for nested dictionary
for i,k in dict4.items():
    for j in k:
        print(j+":",k[j])# ,=>provide automatic space in print
    
print()
#    setdefault()
print("==================set default=============")
dict5={"nadia":"ggggg"} 
dict5.setdefault("age",22)# set default value if key does not exsist if it exsist return old value
print(dict5)

print()
print("=======used in nested dict===============")
school={}
school.setdefault("class1",{}) 
school["class1"].setdefault("student1",{})
school["class1"]["student1"].setdefault("name","nadia")

print(school)

print()
#         fromkeys(): use to add new dict for every key havingsame value 
keys=["name","rollno","subject"]
d=dict.fromkeys(keys,"unknown")
print(d)


