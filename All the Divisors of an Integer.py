n = int(input("Enter the number: "))
print("The divisors are: ")
for i in range(1, 1+n):
    if n%i == 0:
        print(i)