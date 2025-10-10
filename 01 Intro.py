print("hello world") #this is a comment
''' we also can use 3 qoutes for commenting multiple lines'''
a=5
b=8
c=10
d=2.5
result=a+b
print(result)
print(a*c," multiply")
print(10 - 4," subtract")
print(c/d," Divide")
print("Saman"+"Tariq")

#input in python----
c=int(input("enter any integer"))
print(c)

x=str(45) #casting--declare type of variable
z=int(5)
print(x," ", z)

'''we also can get the type of variable using"type()"'''
print(type(x))
print(type(d))

#one value to multiple variable
n=y=r="orange"
print(n+" "+y+" "+r)

#assign multiple values
k,l,t="orange" ,45 ,38.9
print(k+" ",l," ",t)

#EXPRESSION EXICUTION
m,i=3,2
txt='Saman'
print(m*txt*i) #it will  multiply 3and 2 and print saman 6 time 

''''concatination'''
d,y='2',4
tx='uv'
print((d+tx)*y) # add 2uv then print them 4 times

a,b=8,9.0
print(a*b)#float result
v=4
c=2
print(v/c)#always give floating value
print(v//c)# give integer result

# in python we use floor devision rule in which reminder sign depends on denominator sign that make it different from C++ and java 


'''python dosenot have random() function in python we (import random )that is built in module generate random number'''
# random.random() → it gives random float btw 0 and 1 
# random.randint(1,10) → it provide random integer from 1 to 10
# random.randrange(1,10) → it provide randominteger  btw 1 and 10 (exclude 10 from range )
