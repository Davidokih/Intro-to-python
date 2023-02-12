def divide(number1,number2):
    try:
        number1_integer = int(number1)
        number2_integer = int(number2)
        return number1_integer / number2_integer
    
    except ValueError:
        return "Only integers are allowed! Try again"
    
    except ZeroDivisionError:
        return "You cannot divide any number by zero"

number1 = input("Please provide number1: ")
number2 = input("Please provide number2: ")

print(divide(number1, number2))