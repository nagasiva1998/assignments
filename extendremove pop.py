# 5 examples on extend()
l=[10,20,30,40]
l1=[50,60]
l.extend(l1)
print(l)
print()

s=['siva',22,1998,'august']
s1=['age',25]
s.extend(s1)
print(s)
print()

s=['siva',22,1998,'august']
s1=['age',25]
s.extend(s1)
print(s1)
print()

l=[2,4,6,8,10]
l2=[12,14,16,18,20]
l.extend(l2)
print(l)
print()

s=["prabhas is an actor"]
s1=["in tollywood"]
s.extend(s1)
print(s)
print()

#5 examples on remove()
s=["apple","banana","cherry"]
s.remove("banana")
print(s)
print()

l = ["apple", "banana", "cherry", "banana", "kiwi"]
l.remove("banana")
print(l)
print()

animals = ['cat', 'dog', 'rabbit', 'guinea pig']
animals.remove('rabbit')
print('Updated animals list: ', animals)
print()

prime_numbers = [2, 3, 5, 7, 9, 11]
prime_numbers.remove(9)
print('Updated List: ', prime_numbers)
print()

s=['siva',22,1998,'august']
s.remove(22)
print("updated list:",s)
print()
# 5 examples on pop()
list = ["apple", "banana", "cherry"]
list.pop(1)
print(list)
print()

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)# top elememt will be removed
print()

animals = ['cat', 'dog', 'rabbit', 'guinea pig']
animals.pop(2)
print(animals)
print()


prime_numbers = [2, 3, 5, 7]
removed_element = prime_numbers.pop(2)
print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)
print()

languages = ['Python', 'Java', 'C++', 'French', 'C']
removed_element = languages.pop(3)
print('removed value:', removed_element)
print('Updated List:', languages)
print()
# 5 examples on reverse()
languages = ['Python', 'Java', 'C++', 'French', 'C']
languages.reverse()
print(languages)
print()

a = ['cat', 'dog', 'rabbit', 'guinea pig']
a.reverse()
print(a)
print()

systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
systems.reverse()
print('Updated List:', systems)
print()

systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
reversed_list = systems[::-1] # Syntax: reversed_list = systems[start:stop:step] 
print('Updated List:', reversed_list)
print()

l=[10,20,30,40,50]
for i in reversed(l):
    print(i,end=",")
print()    

# 5 examples on sort()
a = ['cat', 'dog', 'rabbit', 'guinea pig']
a.sort()
print("sorting list:",a)
print()

b=[1,9,2,8,4,7,6,5,0]
b.sort()
print(b)
print()

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
print()

numbers = [1, 3, 4, 2]
numbers.sort(reverse=True)
print(numbers)
print()

numbers = [1, 3, 4, 2]
numbers.sort(reverse=False)
print(numbers)

