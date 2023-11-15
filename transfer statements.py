# transfer stements
# 1.break stetement
# 2.continue statement
# 3.pass statement

# break stements 1
for i in range(10):
        print(i)
        if i==4:
         break
print()

# break stement 2       
s="nagasiva"
for letters in s:
     print(letters)
     if letters == "s" or letters == "i":
          break
print("out of forloop") 
print()    

# break statement 3
num= 0
for i in range(10): 
	num += 1
	if num == 8: 
		break
	print("The num has value:", num) 
print("Out of loop") 
print()

# break statement 4
fruits=["apple","banana","promoganate","safota"]
for e in fruits:
      print(e)
      print("siva likes",e)
      if e == "promoganate":
            break
      print('we are likes fruits')
print("out of for loop")      
print()
# break stement 5
# program to find first 5 multiples of 6

i = 1

while i <= 10:
    print('6 * ',(i), '=',6 * i)
    if i >= 5:
        break
    i = i + 1



     
