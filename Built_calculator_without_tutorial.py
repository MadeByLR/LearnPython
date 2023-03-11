#building a calculator

firstNumber = int(input("Enter first number: "))
op = input("Enter operator: ")
secondNumber = int(input("Enter second number: "))
validOperators = ["+", "-", "*", "/"]

if op in validOperators:
    if op == "+":
        print(firstNumber + secondNumber)
    elif op == "-":
            print(firstNumber - secondNumber)
    elif op == "*":
        print(firstNumber * secondNumber)
    elif op == "/":
        print(firstNumber / secondNumber)
else:
     print("Invalid Operator Used!")