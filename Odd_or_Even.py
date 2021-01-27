#Odd or Even
print("-----Odd or even-----")
number = int(raw_input("Wich number should I chek??  "))
modulus = int(number%2)
if modulus >0:
	print("Even!")
if modulus == 0:
	print("Odd!")