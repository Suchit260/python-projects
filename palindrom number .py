num1 = str(input("Enter a number: "))

if num1 == num1[::-1]:
    print(f"The number {num1} is a palidrome")
else:
    print(f"The number {num1} is not a palidrome")