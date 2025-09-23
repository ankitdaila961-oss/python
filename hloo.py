a = float(input("enter your first number"))
b = float(input("enter your second number"))
choice = input("number(+ , - , / , *)")


match choice:
    case "+":
        print("a+b", a + b)
    case "-":
        print("a+b", a - b)
    case "/":
        if b == 0:
            print("can not divide by zero")
        else:
            print("a+b", a / b)
    case "*":
        print("a+b", a * b)
