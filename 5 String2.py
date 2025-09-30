 # In Python we cannot combine strings and number directly{ like we add two strings together}
 #thats why we use ----------f-String and .formate()method-------------

age =19# age=placeholder
print(f"I am {age} old")


print("here we use Formate to show age is=>{a}".format(a=age))
print()
#  A modifier we include with the help of colon like .2f which 
# means fixed pont with 2 decimal'''
price=45
print(f"the whole cabnet price is {price:.2f} dollar")
print("here we also use Formate to tell price is{:.2f}".format(price))

'''we acn also perform math operation inside placeholder'''
print()
print(f"in placeholder we multiply 4 and 5 = {4*5}")
print()

#--------------------Escape Character------------------------
#Escape characters are mainly used in strings to handle formatting and special symbols.
print("using \n move to the new line")
print("it\'s alright")
print()

# we use qoutes inside qoutes with the help of backslash \
print("In future :\"Inshallah\" we won hackthon ")
print()
#\b work as backspace
print("we cant\b do it =>here we remove t in cant")
print()


#---------------Methods in string--------------------------------------
# title() → Capitalizes each word.
# capitalize() → First letter uppercase, rest lowercase.
# count() → Counts how many times substring appears

print("hello world".title())       # "Hello World"
print("python".capitalize())       # "Python"
print("banana".count("a"))         # 3


#lower()->converted into lower case 
#upper()->converted into uppercase
#find()->find word in a string
a="WE WILL PERFORM HAJJ AND UMRAH=>CONVERTED NTO LOWER CASE:"
print(a.lower())
b="say thanks to God for everything=>converted into upper case letter"
print(b.upper())

print(b.find("worship =>here we find word in string"))