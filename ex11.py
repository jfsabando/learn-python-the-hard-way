#We put a , at the end of each print line. This is so print doesn't end the line
#with a newline character and go to the next line.
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print("So you're {} old, {} tall and {} heavy.".format(
	age, height, weight))
	
print("Where are you from?", end=' ')
country = input()

print("I love {}.".format(country))