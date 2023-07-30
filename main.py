def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Division by zero is meaningless")
        return None

def mul(a, b):
    return a*b

while True:
    print("Press A to add")
    print("Press S to subtract")
    print("Press D to divide")
    print("Press M to multiply")
    print("Press Q to Quit")

    operation=input("Enter A, S, D, M, Q to perform arithmetic operations: ")

    if operation=="Q":
        break

    a=int(input("enter first number: "))
    b=int(input("enter second number: "))

    if operation=="A":
        print("Answer: ",add(a, b))
    elif operation=="S":
        print("Answer: ",sub(a, b))
    elif operation=="D":
        print("Answer: ",div(a,b))
    elif operation=="M":
        print("Answer: ", mul(a,b))
    else:
        print("INVALID OPERATION")


