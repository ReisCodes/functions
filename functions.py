# functions

# allow you to follow DRY (Do not repeat yourself)
# def print_something(print_string):
#     print(print_string)
#
#
# print_something("My name is Reis")
# print_something("My second name is Pinnock")
#
#
# def greeting(name):
#     print("Hello, my name is " + name)
#
#
# greeting("Reis")


# Return Statement - Best Practise

# def addition(int1, int2):
#     return int1 + int2
#
#
# print(addition(1, 2))

# Default arguments

# def addition(int1=2, int2=2):
#     return int1 + int2


# print(addition())


# Multiple arguments

# def multi_args(*multiargs):
#     print(type(multiargs))
#
#     for arg in multiargs:
#         print(arg)
#
#
# multi_args(1, 2, 2, 3, 3, 4, 5, 5, "hi")


# type hints

# def greeting(name: str):
#     print("Hello, my name is " + name)
#
#
# greeting("09483")
#
#
# def division(denum: int, num: int) -> float:
#     return denum / num
#
#
# print(division(12, 5))

# Functions best practices

# 1. Name your methods using lowercase and underscores.
# 2. All arguments should be clear in their need and expected type.
# 3. Remember return statement.
# 4. Keep functions as small as possible.
# 5. Use comments within methods to help with clarity on how to use.
# 6. Consider using type hints to avoid errors earlier.

def addition(num1: int, num2: int) -> int:
    return num1 + num2


def subtraction(num1: int, num2: int) -> int:
    return num1 - num2


def multiplication(num1: int, num2: int) -> int:
    return num1 * num2


def division(denum: int, num: int) -> float:
    return denum / num


def convert_cm_to_m(num1: float) -> float:
    return num1 / 100


def convert_m_into_feet(num1: float) -> float:
    return num1 * 3.28084


operators = ["+", "-", "*", "/", "converter"]


def main():
    while True:     # Using a while loop keeps us in the program until correct used
        num1 = input("Please enter your first number: ")     # collect input from users
        num2 = input("Please enter your second number: ")
        if num1.isdigit() and num2.isdigit():                # check if the input is digits
            print("Which Operator Would you like to use:")
            for operator in operators:
                print(operator)
            user_operator_choice = input(": ")
            if user_operator_choice not in operators:        # check if user input is a suitable operator
                print("This is not a valid option, please try again!")
            elif user_operator_choice == "+":                # Calls on each function depending on user choice
                print(addition(int(num1), int(num2)))
                break
            elif user_operator_choice == "-":
                print(subtraction(int(num1), int(num2)))
                break
            elif user_operator_choice == "*":
                print(multiplication(int(num1), int(num2)))
                break
            elif user_operator_choice == "/":
                print(division(int(num1), int(num2)))
                break
            elif user_operator_choice == "converter":
                second_user_choice = input("""Would you like to convert:
                - m - cm to meters
                - f - meters to feet
                : """)
                if second_user_choice == "m":
                    num3 = float(input("What number would you like to convert: "))
                    print(f"{convert_cm_to_m(num3)} Meters")
                    break
                elif second_user_choice == "f":
                    num4 = float(input("What number would you like to convert: "))
                    print(f"{convert_cm_to_m(num4)} Feet")
                    break
                else:
                    print("Please enter a valid option!")
        else:
            print("Please enter valid numbers")


main()
