lower = int(input("Enter the lower number of the range: "))
upper = int(input("Enter the upper numberof the range: "))

for i in range(lower,upper+1):
    if i%2!=0:
        print(i)