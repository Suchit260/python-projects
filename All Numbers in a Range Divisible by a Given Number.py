Upper = int(input("Enter an upper limit: "))
Lower = int(input("Enter a lower limit: "))
n = int(input("Enter a number: "))

for i in range(Lower, Upper + 1):
    if i % n == 0:
        print(i)