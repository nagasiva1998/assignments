# diamond star pattern
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        print('*', end='')
    print()
    # diamond star pattern using 5
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('5', end='')
    print()
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        print('5', end='')
    print()
# right shift pyramid
n = 5
for i in range(n):
    for j in range(i + 1):
        print('*', end="")
    print()
for i in range(n):
    for j in range(n - i - 1):
        print('*', end="")
    print()
# right shift pyramid usin >
n = 5
for i in range(n):
    for j in range(i + 1):
        print('>', end="")
    print()
for i in range(n):
    for j in range(n - i - 1):
        print('>', end="")
    print()
# left shift pyramid
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(i + 1):
        print('*', end='')
    print()
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for k in range(n - i - 1):
        print('*', end='')
    print()

# left shift pyramid using <
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(i + 1):
        print('<', end='')
    print()
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for k in range(n - i - 1):
        print('<', end='')
    print()    