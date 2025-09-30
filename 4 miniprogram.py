# write a program for reversing a sentence
string="this is a coffe shop"
s=string.split()
r=len(s)
t=''
for x in  range(r-1,-1,-1):
 t=t+" "+s[x]
print(t) 
print("-----------------------1----------------------------------")
# The list of non-negative integers that are less than  is . 
#  Print the square of each number on a separate line.
# 0
# 1
# 4
n = int(input("enter any integer = "))
for x in range (n):
      print(x*x)

print("-------------------------2--------------------------------")
import time

for i in range(5):
    print(f"Loading {i+1}/5\r", end="")
    time.sleep(0.5)

 
print("-------------------------3--------------------------------")
#take a input 1)if it is odd print(Weird) ..
# 2)if it is even from 2to 5 then print (Notweird)
# 3)if it is even from 6  to 20 print (weird )
# 4)if it is even and greater than 20

b = int(input().strip())# here we use .strip() to remove an extra space from input like("  24")
if (b%2!=0):
 print("Weird")
elif(b%2==0 and (b>=2 and b<=5)):
 print("Not Weird")
elif(b%2==0 and (b>=6 and b<=20)):
 print("Weird")
elif(b%2==0 and b>=20):
 print("Not Weird")

print("-------------------------4--------------------------------")

#if t=5 the print the constraint 12345
t=int(input("enter any number"))
for i in range(t):
    i=i+1
    print(i,end="") #using end hlp to print in one line
    
print()
print("---------------------------------5---------------------------------------")

# Program to store and display student marks using dictionary

students = {
    "Ali": 85,
    "Sara": 92,
    "hudabia": 89,
    "Saman Tariq": 95   # Added your name with marks
}

for name, marks in students.items():
    print(name, "scored", marks)
  
print()
print()


print("---------------------------------6---------------------------------------")
# Program to swap values using tuple

a = 5
b = 10
print("Before Swap: a =", a, " b =", b)

(a, b) = (b, a)

print("After Swap: a =", a, " b =", b)

print()
print()


print("---------------------------------7---------------------------------------")
# Program to filter even numbers from a list

numbers = [10, 15, 20, 25, 30, 35, 40]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Original List:", numbers)
print("Even Numbers:", even_numbers)
