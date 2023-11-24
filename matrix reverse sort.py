# examples on reverse sort()
numbers = [1, 3, 4, 2]
numbers.sort(reverse=True)
print(numbers)
print()

l=[1,5,2,4,3,8,6,9,7]
l.sort(reverse=True)
print(l)
print()
# examples on copy()
prime_numbers = [2, 3, 5,11]
numbers = prime_numbers.copy()
print('Copied List:', numbers)
print()

my_list = ['cat', 0, 6.7]
new_list = my_list.copy()
print('Copied List:', new_list)
print()

# comparing list objects using == opertor
l1=[1,2,3,4]
l2=[3,1,4,2]
l1.sort()
l2.sort()
if (l1==l2):
    print("equal")
else:
    print("not equal")    
print()

s=[2,4,6,8]
n=[1,3,5,7]
if(s==n):
    print("equal")
else:
    print("not equal")
print()    

# matrix()
n=[[10,20,30],[30,40,50],[60,70,80]]
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[j][i],end=' ')
    print()    

s=[[1,2,3],[4,5,6],[7,8,9]]
for a in range(len(s)):
    for b in range(len(s[a])):
        print(s[a][b],end=" ")
    print()    
# comprehensive 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x) # only the elements containing the letter "a" will be output
print(newlist)
print()

l=["123","234","345","245",'289']
s=[]
for j in l:
    if "2" in j:
        s.append(j)
print(s) 
print()       

#square root of range from 1 to 20
l=[x*x for x in range(1,21)]
print(l)
# do some action in l1 and use l1 in l2
l1=[x*x for x in range(1,11)]
print(l1)
l2=[i for i in l1 if i%2==0]
print(l2)
 


