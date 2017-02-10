#set a string with format and assign a variable
formatter = "{} {} {} {}"

#Assign a number for each of the placeholders
print(formatter.format(1, 2, 3, 4))
#assign a string for each of the placeholders
print(formatter.format("one", "two", "three", "four"))
#assign a boolean for each of the placeholders
print(formatter.format(True, False, False, True))
#treat formatter inside the format as a string
print(formatter.format(formatter, formatter, formatter, formatter))
#assign a string for each of the placeholders"
print(formatter.format(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
))
