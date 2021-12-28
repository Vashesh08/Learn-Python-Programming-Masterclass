import sys


def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        except:  # Should be except ValueError:
            print("Invalid Number Entered. Please Try Again:")
        finally:
            print("The finally clause always execute")


def divide_numbers(a, b):
    # while True:
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Cannot Divide by Zero.")
        sys.exit(2)
        # b = get_int("Please Enter Valid Second Number:")
    else:
        print("Division performed successfully")


first_number = get_int("Please Enter First Number:")
second_number = get_int("Please Enter Second Number:")
divide_numbers(first_number, second_number)
