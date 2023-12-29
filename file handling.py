#read

f=open("siva.txt","r")
print(f.read())

f=open("siva.txt","r")
print(f.read(10))

#write

f1=open("ram.txt","w")
print(f1.write("hell world"))

#append

f=open('a2.txt',"a")
print(f.write("how are you every one")) 

#r+
f=open("r1.txt","r+")
print(f.read())

#w+

f=open("w1.txt","w+")
print(f.write("python programming"))


#r+w+

f1=open("rw1.txt","r+")
print(f1.write("helloworld"))

#a+

f1=open("append1.txt","a+")

print(f1.write("helloworld"))
