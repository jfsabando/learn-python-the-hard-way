#assign values to cycle through the different loops
people = 30
cars = 40
trucks = 15

#3 conditions are assigned... 
if cars > people:
	print("We should take the cars.")
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decide.")

#3 conditions are assigned
if trucks > cars:
	print("That's too many trucks.")
elif trucks < cars:
	print("Maybe we could take the trucks.")
else:
	print("We still can't decide.")

#2 conditions are assigned	
if people > trucks:
	print("Alright, let's just take the trucks.")
else:
	print("Fine, let's stay home then.")
