#pro to print diff ovels present in the given word and count of ovels
a="my name is nagasiva i am from kadapa"
count=0
for x in a:
    if x in "aeiou":
        count=count+1
        print("count of vowel is :",count,end=" and ")
        print("vowel is", x)
print()        
    
s=input("enter the string :")
l=[x for x in s if x in "aeiou"]
print("count of vowels are ",len(l))
print(l)

#pr to enter the name and % of marks in a dict and display info on the screen 

n=input("enter the name :")
m=int(input("enter the marks :"))
dis={"name":n,"marks %":m}
print(dis)
print()

n = int(input("Enter number of students: "))  

result = {}  

for i in range(n):  

   print("Enter Details of student No.", i+1)   
   name = input("Name: ")  
   marks = int(input("Marks: "))  
   result = {"name":name, "%":marks}   
print(result)  
print()
#write a pro to eliminate duplicates in the list 
a=[2,4,6,8,10,10,6,8,2,4]
print("the original list is :",a)
l=[]
for i in a:
    if i not in l:
        l.append(i)
print("the list after removing duplicate values :",l)        





















