print('Hi, welcome to the calculator')

numberOne = float(input('Enter a number:  '))
numberTwo = float(input('Enter another number: '))

typeOperation = input('What type of operation do you want to perform? addition(a), subtraction(s), multiplication(m), or division?(d): ')


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Error: division by zero'


if typeOperation == 'a':
    print(addition(numberOne, numberTwo))
elif typeOperation == 's':
    print(subtraction(numberOne, numberTwo))
elif typeOperation == 'm':
    print(multiplication(numberOne, numberTwo))
elif typeOperation == 'd':
    print(division(numberOne, numberTwo))
else:
    print('Oops.. something went wrong.')
