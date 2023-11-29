# multiply the tuple with 2
l=(10,20,30,40,50)
print(l*2)
#types of tuple we can write
t=(10,20,30,40)
print(type(t))

t=10,20,30,40
print(type(t))

t=10
print(type(t))

t=10,
print(type(t))

t=()
print(type(t))

t=(10)
print(type(t))

t=(10,)
print(type(t))

# vowels

text = "python is a not an easy untill we will practice"
l = [char for char in text if char in "aeiou"]
print(len(l))   
print(l)  
print()

text ="ys jagan is a cm of ap"
for char in text:
    if char in 'aeiou':
        print(char) 
print()        
#write a pro to take tuple of numbers from keyboard and print Sum,avg
t=(10,15,20,25,30,35,40,45,50,55)
sum=0
for i in t:
   sum=sum+i
print(sum)

t=(10,15,20,25,30,35,40,45,50,55)
sum=0
avg=len(t)
for i in t:
    sum=sum+i
print(sum/avg)





