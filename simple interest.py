principle = float(input("What is the principle amount: "))
rate = float(input("What is the rate of interest: "))
time = float(input("What is the time in years: "))

simple_interest = (principle * rate * time) / 100
print(f"Simple Interest: ${simple_interest}")

total_amount = principle + simple_interest
print(f"Total Amount after {time} years: ${total_amount}")
