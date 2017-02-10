print("You see a beautiful girl on the coffee line. What do you do?")
print("1. Approach and say hi.")
print("2. Look away and 'answer' messages on cell phone.")
approach = input("> ")

if approach == "1":
	print("Nice job! She said hi back and talk some time. What do you do now?")
	print("1. Ask for her phone number.")
	print("2. Tell her to have a nice day and go away.")
	
	conversation = input("> ")
	
	if conversation == "1":
		print("Good! You have her number and a possible date.")
	elif conversation == "2":
		print("So, so... You just had a nice moment and that's it")
	else:
		print("Don't be gay, do something...")

elif approach == "2":
	print("Make something different and go for it!")

else:
	print("There are only 2 options genius")