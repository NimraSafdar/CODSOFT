def addition(number1, number2):
    answer = number1 + number2
    return answer

def subtraction(number1, number2):
    answer = number1 - number2
    return answer

def multiplication(number1, number2):
    answer = number1 * number2
    return answer

def division(number1, number2, division_type):
    try:
        if division_type.upper() == "INTEGER":
            answer = number1 // number2
        elif division_type.upper() == "FLOAT":
            answer = number1 / number2
        return answer
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

print("Simple Calculator")
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter your required operation (addition, subtraction, multiplication, division): ")

if operation.lower() == "addition":
    result = addition(first_number, second_number)
elif operation.lower() == "subtraction":
    result = subtraction(first_number, second_number)
elif operation.lower() == "multiplication":
    result = multiplication(first_number, second_number)
elif operation.lower() == "division":
    division_type = input("Enter division type (integer or float): ")
    result = division(first_number, second_number, division_type)
else:
    result = "Invalid operation"

print(f"Your output of {operation} on {first_number} and {second_number} is {result}")
