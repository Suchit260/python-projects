operator = input("Enter the operator: ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operator == "+":
    sum = num1 + num2
    print(f"Result: {sum}")
elif operator == "-":
    diff = num1 - num2
    print(f"Result: {diff}")
elif operator == "/":
    result = num1/num2
    print(f"Result: {result}")
elif operator == "*":
    product = num1 * num2
    print(f"Result: {product}")
else:
    print("Not a valid operator.")
