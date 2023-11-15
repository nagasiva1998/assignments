# 1.write a pro to find the biggest of given 2 numbers from the keyboard
a=int(input("enter the 1st number :"))
b=int(input("enter the 2nd number :"))
if a>b:
    print(a,"the biggest value")
else:
  print(b,"the biggest value")


#2.program to check whether the given number is in between 1 to 100
a=int(input("enter the value :"))
j="value is in" if a<=100 else "value not in"
print(j)

# 3.write a program some digit entered by user and it should be in words
c=int(input("enter the value :"))
if c==1:
    print("one")
elif c==2:
    print("two")
elif c==3:
    print("three") 
elif c==4:
    print("four") 
elif c==5:
    print("five")
else:
    print("none")