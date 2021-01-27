print("----Divisors----")
number = int(raw_input("Number pls: "))
divisor = 2
print("1")

while number > divisor:
	op = number % divisor
	if op == 0:
		print(divisor)
	divisor = divisor + 1
print(number)


