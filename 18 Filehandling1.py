#============file handling/////////

f=open("demo.txt","rt")  #open file
print(f.read())#read the text in the file
f.close() #close file

#============closing file without using ========f.close()===============

print("===========open file by given path============== ")

with open(r"C:\Users\LAPTOOL TECHNOLOGY\OneDrive\Documents\pyvibes.txt.txt") as file:
    print(file.read())
    
    


print("==== ================== Returns character of the string  ================== =====")
with open("demo.txt") as f1:
    print(f1.read(5))
    
print()
#readline()=>read a line at the basis of current cursor  
print("========Readline===============")
with open(r"C:\Users\LAPTOOL TECHNOLOGY\OneDrive\Documents\pyvibes.txt.txt") as f2:
    print(f2.readline()) #print 1st line if you want 2nd line also write it again
    print(f2.readline()) 
    print(f2.readlines())# it will convert all lines into list also empty lines(a little bit messy we clen it using logic)
    
  
print()  
print("============using loops==================")    
with open("demo.txt") as f3:
    for line in f3:
        print(line)