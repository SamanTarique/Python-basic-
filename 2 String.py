''' Python does not have a character data type, a single character is simply a string with
a length of 1.Square brackets can be used to access elements of the string.'''

#--------------------it will print a (like indexing in array where counting start from 0)-----------------------------------------------------------------
p="Saman"
print(p[1])

'''-----------------check length using(len())-------------------------------------------------'''
print (len(p))

'''--------------#check word present in string provide boolean answer true or false----------------------------------------------------'''


book="After independence we are free to go any where in our country"
print("free" in book) #here we use( in )keyword to find free word in above text store in book 

'''---------------#check word not present in the string using (not in)---------------------------------------------------'''


print ("Prayer" not in book) #=>true
print()

#---------------------------===SLICING STRING===---------------------------------------------------------------

'''Slicing String: start index and the end index, separated by a colon, to return a part of the string.'''

a="Saman tariq"
print(a[2:7]) #print from 2 to 5 index

#by leaving starting index it will print from start same when ''leave end index (we can leave a value in range)
print(a[:7],"=>leaving starting")
print(a[2:],"=>leaving end")

''' Negative indexing :count from right side (-1) '''
b="ethics and manners"
print(b[-15:-1], "=>negative index")

print()


#---------------------------===MODIFY STRING-===--------------------------------------------------------------
b="converted to upper case letter"
print(b.upper())

c="CONVERTED INTO LOWER CASE"
print(c.lower())

d="     using strip() it will remove white space from start and end of our string       "
print(d.strip())

e="#########we can also remove spacific character from starting and end of string using stip()########"
print(e.strip("#"))

print()

# using replace():we can replace a word or character from the string 
f="here is hard word replace "
print(f.replace("hard","easy"))
print(f.replace("h","k"))
print()

#using split(): we can split the specified string words and converted into list 
g="here we, convert string into list"
print(g.split())# by default it will take white space
print()
print(g.split(","))#here seprate where is comma


