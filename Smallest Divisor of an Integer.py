n = int(input("Enter an integer: "))
a = []
for i in range(1, n+1):
    if n%i == 0:
        a.append(i)
a.sort()
print("smallest divisor: ", a[0])