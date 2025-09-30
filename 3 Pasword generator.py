 #python doesnot generate any character or symbols randommly we want to import or
 # write them in our program
import string
import random

print(string.ascii_letters) 
print(string.punctuation)
char=string.ascii_letters+string.punctuation

enter= int(input("enter the length of pasword"))
pasword=""
for x in range(enter):
  pasword=random.choice(char)+pasword
  
print(pasword)
 
