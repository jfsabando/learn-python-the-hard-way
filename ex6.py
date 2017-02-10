#Assign a variable x Make a string and set 10 instead of {}
x = "There are {} types of people.".format(10)
#Assign variables with strings
binary = "binary"
do_not = "don't"
#Assign a variable y a string that calls other strings - 1,2
y = "Those who know {} and those who {}.".format(binary, do_not)

#print the previous assigned variables
print(x)
print(y)

#print a string that calls a variable(string) - 3
print("I said: {}.".format(x))
#print a string that calls a variable(string) - 4
print("I also said: '{}'.".format(y))

#set a boolean value
hilarious = False
#set a variable that calls another string
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"
#concatenate the variables
print(w + e)