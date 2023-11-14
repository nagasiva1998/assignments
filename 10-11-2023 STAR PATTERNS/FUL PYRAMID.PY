# using * 
n = 5
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print("*", end=" ")
	print()
# triangle
def triangle(n):
	k = n - 1
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 1
		for j in range(0, i+1):
			print("* ", end="")
		print("\r")
n = 5
triangle(n)
# alphabetics
n = 5
alph = 65
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print(chr(alph), end=" ")
		alph += 1
	alph = 65
	print()
	
# using i values
n =5
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print(i, end=" ")
		i += 1
	print()
# using j values
n = 5
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print(j, end=" ")
	print()
	
# using H
n = 5
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print("H", end=" ")
	print()    

# using siva
n = 6
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print("siva", end=" ")
	print()
# using @
n = 6
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print("@", end=" ")
	print()	
# using 5
n =6
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print("5", end=" ")
	print()		
	
# using 123
n =6
for i in range(0, n):
	print(" " * (n-i), end=" ")
	for j in range(0, i+1):
		print("123", end=" ")
	print()		
	    
	
	
	
	
    


