# continue stetement 1
for i in range(5):
    if i == 2:
        continue
    print(i)
print()

# continue stetement 2
num=0
while num<10:
    num +=1
    if num %2==0:
        continue
    print(num)
# continue stetement 3
for i in range(20):
    if i%2!=0:
        continue
    print(i)

 # continue statement 4
num= 0
for i in range(10): 
	num += 1
	if num == 8: 
		continue
	print("The num has value:", num) 
print("Out of loop") 
print()
# continue statement 5
cart=[20,30,40,500,600,10]
for item in cart:
     if item>500:
          print("exeeds the limit",item)
          continue
     print("processing item succesfully",item)

    