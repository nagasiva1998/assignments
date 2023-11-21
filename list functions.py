# 5 examples on index

name="python is a programming language and it is very simple"
print(name.index("is"))
print(name.index("y"))
print(name.index("la"))
print(name.index("a",0,15))
#print(name.index("z"))#substring not found error
# 5 examples on insert
l=[2,4,6,8,10]
l.insert(3,20)
print(l)

l=[2,4,6,8,10]
l.insert(2,30)
print(l)

l=[1,2,3,4,5,6,7]
l.insert(4,15)
print(l)

l=[10,20,30,40,50,60]
l.insert(5,90)
print(l)

l=[1,3,5,7,9,11]
l.insert(1,2)
print(l)

#5examples on count
name="python is a programming language and it is very simple"

print(name.count("a"))
print(name.count("is"))
print(name.count("are"))
print(name.count("b"))
print(name.count("ve"))
print(name.count("vet"))

# 5 examples on append method

l=[2,4,6,8,10]
l.append(9)
print(l)

l=[2,4,6,8,10]
l.append(55)
print(l)

l=[1,2,3,4,5,6,7]
l.append(44)
print(l)

l=[10,20,30,40,50,60]
l.append(66)
print(l)

l=[1,3,5,7,9,11]
l.append(88)
print(l)

l=[]
j=10,20,30
l.append(j)
print(l)

# 3 examples on list using for loop
l=[10,20,30,40,50]
for i in l:
    print(i)
print()    

l=[11,12,13,14,15,16]
for i in l[2:5]:
    print(i)
print()

l=[1,2,3,4,5,6,7,8]
for i in l[::-1]:
    print(i)
print()    

# acceing elements using while loop
l=[2,3,4,5,6,7,8,9]
i=0
while i<len(l):
    print(i)
    i=i+1
print()

l=[10,20,30,40,50]
s=0
while s<len(l):
    print(l[s])
    s=s+1
print()    

l=[10,20,30,40,50,60]  
i=0
while i<len(l[1:5]):
    print(l[i])
    i+=1  



