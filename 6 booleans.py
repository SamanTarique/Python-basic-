#When you compare two values, the expression is evaluated and Python returns the Boolean answer:(true,False)
a,b=6,7
print(a==b,": boolean answer1")
print(a<b,"2result")
print()

# bool():mostly allow you evalute true false except when we have (0,"",[], (), {})in  this condition answer will false
print(bool('hello world'),"3 result")
print (bool(" "),"4 result")

# one more case it will return a false value if you have  function that returns 0
''' here ! we created class and inside function it return zero that gives us False answer '''
class mylec():
    def My1(self):#function
        return 0#false
myobj=mylec()
print(bool(myobj),"=>boolean result5")
print()
#in python we use isinstance function to check the value of certain datatype that will reult boolean answer true or false

x="Saman"
print(isinstance(x,str),"6 result")

#operator >>=,<<=,:= 
# Right shift assigment :in programing we use right shift (x>>=1)=(x=x//2) when we need fast division by 2  
# Left shift assigment :we use it for fast multiplication(x<<=1)=(x=x*2)
print()
x=4
x>>=1
print(x," =divided")
x<<=1
print(x," =Multiply")

# Walrus operator.(one line operator )we use this operator inside the expression(if ,while,print())
# donot use it as assigment operator.

print(t:=len("Saman"),"here we use walrus operator")







