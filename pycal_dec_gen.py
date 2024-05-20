def calculator(func):
    def wrapper(*args, **kwargs):
        #print("Calculator process initiated")
        result = func(*args, **kwargs)
        #print("Calculator process Terminated")
        return result

    return wrapper


@calculator
def add(num1, num2):
    return num1 + num2


@calculator
def subtract(num1, num2):
    return num1 - num2


@calculator
def multiply(num1, num2):
    return num1 * num2


@calculator
def division(num1, num2):
    sol = num1 / num2 if num2 != 0 else "Error:Zero Division Error"
    return sol


def in_generator():
    while True:
        opp = input("Choose any of the above opperation to perform \n1.add\n2.subtract\n3.multiply\n4.division\n5.Exit \nInput:  ")
        if opp == 'Exit':
            break
        else:
            if opp in ['add', 'subtract', 'multiply', 'division']:
                num1 = float(input())
                num2 = float(input())
                yield opp, num1, num2
            else:
                print("Selected opperation not supported")


def calculator_function():
    for opp, num1, num2 in in_generator():
        if opp == "add":
            result = add(num1, num2)

        elif opp == "subtract":
            result = subtract(num1, num2)
        elif opp == "multiply":
            result = multiply(num1, num2)
        elif opp == "division":
            result = division(num1, num2)
        print("\nResult: ", result)


calculator_function()
