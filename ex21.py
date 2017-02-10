def add(a, b):
	print("ADDING {} + {}".format(a, b))
	return a + b
 
def substract(a, b):
	print("SUBSTRACTING {} - {}".format(a,b))
	return a - b
 	
def multiply(a, b):
	print("MULTIPLYING {} * {}".format(a, b))
	return a * b
 	
def divide(a, b):
	print("DIVIDING {} / {}".format(a, b))
	return a / b
 
 	
print("Let's do some math with just functions!")
 
#age = add(float(input()),float(input()))
age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
 
print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))
 
 
# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")
 
what = add(age, substract(height, multiply(weight, divide(iq, 2))))
 
 
print("That becomes: ", what, "Can you it by hand?")

def newfunc(age, height, weight, iq):
	return age + (height - (weight * (iq / 2)))
	
what2 = newfunc(age, height, weight, iq)
print(what2)