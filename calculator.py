a = int(input("1st Number:"))
b = int(input("2nd Number:"))
c = input("Operator:")
if c == "+":
    print(a, c, b, "=", a + b)
if c == "-":
    print(a, c, b, "=", a - b)
if c == "×" or c == "*":
    print(a, c, b, "=", a * b)
if c == "÷" or c == "/":
    print(a, c, b, "=", a / b)
