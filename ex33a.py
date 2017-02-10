def while_func(var, inc):

	i = 0
	numbers = []

# 	while i < var:
	for i in range(var):
		print("At the top i is {}".format(i))
		numbers.append(i)

# 		i = i + inc
		print("Numbers now: ", numbers)
		print("At the bottom i is {}".format(i))

	print("The numbers: ")

	for num in numbers:
		print(num)
		
while_func(6, 1)
while_func(5, 2)
while_func(20, 4)
while_func(30, 6)