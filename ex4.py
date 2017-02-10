#assign the variable cars a value
cars = 100
#assign the variable space in a car a value
space_in_a_car = 4.0
#assign the number of drivers to the variable
drivers = 30
#assign the number of passengers to a variable
passengers = 90
#perform a math operation with the previously defined variables
cars_not_driven = cars - drivers
#assign a variable another variable
cars_driven = drivers
#assign a math operation result a variable
carpool_capacity = cars_driven * space_in_a_car
#perform a math operation
average_passengers_per_car = passengers / cars_driven

#print and concatenate
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")