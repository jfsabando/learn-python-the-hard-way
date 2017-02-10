from sys import argv

script, filename = argv

txt = open(filename)
print("Here's the contents of {}:".format(filename))
print(txt.read())