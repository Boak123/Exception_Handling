"""Write a program that:

Asks the user for two numbers.
Divides the first number by the second.
Handles:
ValueError
ZeroDivisionError
If no error occurs, print the result.
Always print:
    Thank you for using the calculator.
Use:

try
except
else
finally
"""


try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Invalid input. Please enter integers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(result)
finally:
    print("Thank you for using the calculator.")
while question := input("Do you want to calculate again? (yes/no): ").lower() == "yes":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter integers only.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(result)
    finally:
        print("Thank you for using the calculator.")
