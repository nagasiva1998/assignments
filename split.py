# program to reverse a string using split function
s="rangerover is a beast"
r= reversed(s.split(" "))
for x in r:
    print(x,end=" ")
print()

#program to reverse a string using split function
s="rangerover is a beast"
r=s.split()
for x in r[::-1]:
   print(x[::-1],"",end="")
print()   
    
#program to reverse a string using split function
s="rangerover is a beast"
r=s.split(" ")
for x in r[::-1]:
    print(r[::-1]," ",end="")
print()

# lower,upper,swapcase,capitalize,title.
# lower()
a="NAGASIVA"
print(a.lower())
b="Nagasiva"
print(b.lower())
# upper()
c="nagasiva"
print(c.upper())
d="Jagan"
print(d.upper())
# swapcase()
e="DURGAPRIYA"
print(e.swapcase())
f="durgapriya"
print(f.swapcase())
g="DuRgA"
print(g.swapcase())
#capitalize()
str="try a new recipe"
print(str.capitalize())
name="make a bucket list"
print(name.capitalize())
#title()
str="try a new recipe"
print(str.title())
name="make a bucket list"
print(name.title())