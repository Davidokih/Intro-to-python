import test
import seaborn as sns
import math

def hello(name):
    print("hello", name)

# hello("David")

def sum(number1,number2):
    answer = number1 + number2
    return(answer)

# print(sum(5,3))

# test.greetings("David")

data = [1, 2, 10, 3, 5, 6, 13]

# sms.lineplot(range(7), data)
# sms.lineplot(data,range(7))

# Argument in python

def argument_printer(argument1,argument2):
    print("Argument at position 1:", argument1)
    print("Argument at position 2:", argument2)

# argument_printer("Value 1", "Value 2")

def greetings(first_name,last_name, auto_correct = True):
    if auto_correct == True:
        capitalize_first_name = first_name.capitalize()
        capitalize_last_name = last_name.capitalize()
        print("Hello", capitalize_first_name, capitalize_last_name)
    else: 
        print("Hello", capitalize_last_name,last_name)

greetings("david","okih")

def car(brand,model,color):
    print("my favourite car is", brand, model, "in color", color)

car("Tesla", "320", "black")
# Keyword argument
car(color="black", brand="Tesla", model="356")

# Local and Global scopes

# Global Scope
number = 13

def change_number():
    number = 4

# It will still return the global variable
change_number()
print("It will return 13:",number)

def change_number2():
    global number
    number = 4

change_number2()
print("It will return 4:",number)


def difference(number1, number2):
  #Write a function that calculates the difference between two numbers
  diff = number1 - number2
  return diff

#Call the difference function to calculate the difference between the chocolate prices
difference(14.99 , 12.49)

#Run this cell to store Julia's personal information in variables
birthday = "4 September 1996"
place_of_birth = "London"
current_city = "London"

#Write an introduction function that takes birthday, place_of_birth and current_city as arguments
def introduction(day_of_birth,birth_place,city_live_in,name):
#and prints the sentence above
  print("Good day my name is", name, "i was born", day_of_birth, "in",birth_place, "i currently live at",  city_live_in)

#Call the introduction function 
introduction(birthday, place_of_birth, current_city, "Julia")

#Write a function to change the current_city 
def change(new_city):
  global current_city
  current_city = new_city
  return current_city

#Change current_city to "New York"
change("New York")

#Call the introduction function 
introduction(birthday, place_of_birth, current_city, "Julia")

#Weather data 
day = [1, 2, 3, 4, 5, 6, 7]
avg_temperature = [14,9,3,11,18,27,6]

#Create a bar plot for the given data
sns.barplot(day,avg_temperature)

def mile2km(miles):
  #Write a function to convert miles to kilometers 
  km = miles * 1.60934
  return km

def km2mile(km):
  #Write a function to convert kilometers to miles
  mile = km / 1.60934
  return mile

### RUN THIS CELL TO TEST YOUR IMPLEMENTATION
assert math.isclose(mile2km(132.2), 212.754748, abs_tol=1e-5), "Test failed for mile2km!"
assert math.isclose(km2mile(48.44), 30.099295, abs_tol=1e-5), "Test failed for km2mile!"
print("Test passed!")

#Call the mile2km function to convert 12 miles
mile2km(12)

def pound_kilogram(quantity, mode):
  assert mode == "pound2kg" or mode == "kg2pound", "Invalid argument!"
  #Here the assert command ensures that a valid mode is given as argument.
  if(mode == "pound2kg"):
    #Write a statement to convert pound to kilogram for mode "pound2kg"
    convert = quantity * 0.45359

    #Else it should convert kilogram to pound
  else:
    convert = quantity / 0.45359
  return convert

### RUN THIS CELL TO TEST YOUR IMPLEMENTATION
assert math.isclose(pound_kilogram(2.20462, "pound2kg"), 1, abs_tol=1e-5), "Test failed for mode \"pound2kg\"!"
assert math.isclose(pound_kilogram(43, "kg2pound"), 94.79926, abs_tol=1e-5), "Test failed for mode \"kg2pound\"!"
print("Test passed!")

#Call the function to convert 2 kilograms to pound
pound_kilogram(2, "kg2pound")

def fahrenheit_celcius(temperature, mode):
  assert mode == "f2c" or mode == "c2f", "Invalid argument!"
  # Write a statement to convert Fahrenheit to Celsius or Celsius to Fahrenheit
  if mode == "f2c":
    convert = (temperature - 32) * 5/9
  else:
    convert = (temperature * 9/5) + 32
  return convert

### RUN THIS CELL TO TEST YOUR IMPLEMENTATION
assert math.isclose(fahrenheit_celcius(98.6, "f2c"), 37.0, abs_tol=1e-5), "Test failed for mode \"f2c\"!"
assert math.isclose(fahrenheit_celcius(42, "c2f"), 107.6, abs_tol=1e-5), "Test failed for mode \"c2f\"!"
print("Test passed!")

#Call the function to convert 88° Fahrenheit to Celsius
fahrenheit_celcius(88, "c2f")