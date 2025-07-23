import time
seconds = int(input("Enter the countdown time in seconds: "))


for i in range(seconds, 0, - 1):
    print("Time left: ", i, "seconds")
    time.sleep(1)

print("Time's up")

# while seconds > 0:
# print("Time left: ", seconds, " seconds")
# time.sleep(1)
# seconds -= 1
# print("Time's up")
