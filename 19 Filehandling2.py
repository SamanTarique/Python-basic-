# create file 
#f=open("myfile.txt","x")

# "a":append text at the end of existing text
with open("myfile.txt","a") as f:
    f.write("we are adding newlines here")
    

with open("myfile.txt")as f3:
    print(f3.read())
  
print()  

#2nd Method================================================================

print("======with method2=========")

with open("myfile.txt","a+") as file:
    file.write("ok we will add it soon for reading line move it toward o cursor")
    file.seek(0)#it will move your cursor 
    print(file.read())
    
    # 0=>move cursor at start of the file
    # 1 => start from current position of file
    # 2 => cursor move  end of file    f.seek(0,2)
    

print()# delete existing text or replace whole existing text or overwrte existing content
with open("myfile.txt","w+") as f:
    f.write("Oops! written content is deleted")
    f.seek(0)       # cursor moves  towardstart 
    print(f.read()) 
 
 
    
    
    
    
    
