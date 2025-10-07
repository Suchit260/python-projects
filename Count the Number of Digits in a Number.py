n = int(input("Enter the number: "))
count = 0
while n>0:
    count = count+1
    n = n//10

print(f"Number of digits in the number: {count}")