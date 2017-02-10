#use the argv to assign the filename to a variable
from sys import argv

script, filename = argv

#use the file given by argv, save it in the variable txt (it's a file)
txt = open(filename)

#show the string and the name of the file
print("Here's your file {}:".format(filename))
#show the contents of the file
print(txt.read())






#asks for the filename in a different way
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()