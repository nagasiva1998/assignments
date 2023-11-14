# reverse pyramid pattern
n = 5
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(n-i)+1):
        print('*', end='')
    print()
# reverse pyramid pattern i values
n = 5
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(n-i)+1):
        print(i, end='')
    print()    
# reverse pyramid pattern j values
n = 5
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(n-i)+1):
        print(j, end='')
    print()
# reverse pyramid pattern alphabets
n = 5
alph=65
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(n-i)+1):
        print(chr(alph), end='')
        alph+=1
    print()    
# reverse pyramid pattern using &
n = 5
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(n-i)+1):
        print('&', end='')
    print()
# reverse pyramid pattern using RAM
n = 5
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(n-i)+1):
        print('RAM', end='')
    print()    
# reverse pyramid pattern using ^
n = 5
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(n-i)+1):
        print('^', end='')
    print() 
# reverse pyramid pattern using 45
n = 5
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(n-i)+1):
        print('45,', end='')
    print() 
# reverse pyramid pattern using @
n = 5
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(n-i)+1):
        print('@,', end='')
    print() 
# reverse pyramid pattern using >
n = 5
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end='')
    for j in range(2*(n-i)+1):
        print('>', end='')
    print() 
           
           
              