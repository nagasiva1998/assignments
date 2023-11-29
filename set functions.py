a=(10,20,30,40) # it is not a set
s=set(a) # it is converted into set
print(s)
print(type(s))
print()
#add()
s={1,2,3,4,5}
s.add(10)
s.add(20)
s.add("siva")
print(s)
print()
#a={}
#a.add('ram')
#print(a)  here we get an attribute error
a={"ram",'jagan'}
a.add("ram")
a.add('RAM')
a.add('Jagan')
print(a) # set is not allowed duplicate values
b={10.2,20.5,30}
b.add(10)
b.add(99.9)
print(b)
print()
c={10,25,30,35}
c.add('siva123')
# c.add('ram',12) here we get type error set takes one argument only
print(c)

# remove()
s={1,2,3,4,5}
s.remove(1)
s.add(2)
print(s)
print()
a={'siva','jagan','ram',10,25}
a.remove(10)
a.remove(25)
print(a)
print()
b={2,4,6,8,10,11,13}
b.remove(11)
b.remove(13)
print(b)
print()
c={1,5,7,11,20}
c.remove(20)
#c.remove(24) here we get key error 
print(c)
print()
# update()

x={10,20,30}
y={40,50,60}
x.update(y)
print(x)
print()

a={"apple","banana"}
b={"lemon","cherry"}
a.update(b)
print(a)
print()
c={1,2,3,4,5}
d={'a','b','c','d','e'}
c.update(d)
print(c)
print()

e={'aman','ram','siva'}
f={'aman','jagan','durga'}

e.update(f)
print(e)
print()
#pop()
l= {"apple", "banana", "cherry"}
print(l.pop())
print(l.pop())
      

t = {"apple", "banana", "cherry"}
t.pop()
print(t)
print()

animals = {'cat', 'dog', 'rabbit', 'guinea pig'}
animals.pop()
print(animals)
print()


prime_numbers = {2, 3, 5, 7}
removed_element = prime_numbers.pop()
print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)
print()
