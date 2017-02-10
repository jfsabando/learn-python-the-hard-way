name = 'JF Sabando'
age = 27 # not a lie
height = 68.11 # inches
height_c = round(height * 2.54, 2) #centimeters
weight = 171 # lbs
weight_k = round(weight * .45, 2) # kilograms
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print("Let's talk about {}.".format(name))
print("He's {} inches tall.".format(height))
print("He's {} pounds heavy.".format(weight))
print("He's {} centimeters tall.".format(height_c))
print("He's {} kilograms heavy.".format(weight_k))

print("Actually that's not too heavy.")
print("He's got {} eyes and {} hair.".format(eyes, hair))
print("His teeth are usually {} depending on the coffee.".format(teeth))

#this line is tricky, try to get it exactly right
print("If I add {}, {}, and {} I get {}.".format(
	age, height, weight, age + height + weight))
	