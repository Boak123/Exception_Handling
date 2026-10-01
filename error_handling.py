try:
    num = int(input("Enter a Number: "))
    print(f"You enter {num}")
except ValueError:
    print("Invalid Number")


#2

try:
    num1 = int(input("Enter a firstnum: "))
    num2 = int(input("Enter a second num: "))
    result = num1 / num2
    print(result)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Cannot divide by zero.")

#3

try:
    numbers = [1, 2, 3]

    number = int(input("Enter index: "))

    print(numbers[number])

except ValueError:
    print("Please enter a valid number.")

except IndexError:
    print("Index does not exist.")

#4



