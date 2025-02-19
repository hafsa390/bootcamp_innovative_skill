# You are building a calculator app. Write a Python function calculate() that takes two
# numbers and an operator (+, -, *, /) as input and returns the result.

def calculate(num1, num2, op):

    # Dictionary of operators and its functions
    ops = {
        '+' : lambda x,y: x + y,
        '-' : lambda x,y: x - y,
        '*' : lambda x,y: x * y,
        '/' : lambda x,y: x /y
    }

    # Performing the operations based on operator
    if op == '+' :
        result = (ops['+'](num1, num2))

    elif op == '-':
        result = (ops['-'](num1, num2))

    elif op == '*':
        result = (ops['*'](num1, num2))

    else:
        result = (ops['/'](num1, num2))

    return result


if __name__ == "__main__":

    # Taking the numbers and operator as inputs from user
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))
    operator = input("Enter the operator: ")

    # Calling the calculate() function
    output = calculate(firstNumber, secondNumber, operator)

    print("The result is", output)
    print("Computing Done.")