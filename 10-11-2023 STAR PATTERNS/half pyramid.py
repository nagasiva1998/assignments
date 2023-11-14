# Program to print half pyramid using *
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")

# Program to print half pyramid a using numbers
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")    
#    Program to print half pyramid using alphabets
rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print("\n")

# Inverted half pyramid using *
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    
    print("\n")

#    Inverted half pyramid using numbers
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    
    print("\n")

#    Inverted half pyramid using A
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print('A', end=" ")
    
    print("\n")    

#    Inverted half pyramid using @
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print('@', end=" ")
    
    print("\n")  
# REVERSE PATTERN
rows = 5
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
      
# REVERSE PATTERN 
rows = 5
for i in range(rows, 0, -1):
    num=i
    for j in range(0, i):
        print('CV', end=' ')
    print("\r")
            
# REVERSE PATTERN j
rows = 5
for i in range(rows, 0, -1):
    num=i
    for j in range(0, i):
        print(j, end=' ')
    print("\r")
                  