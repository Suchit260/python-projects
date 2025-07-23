import time

seconds = int(input("Type in the seconds: "))

for i in range(seconds, 0, -1):
    minute = int(i/60) % 60
    hour = int(i/3600)
    print(f"{hour:02}:{minute:02}:{i:02}")
    time.sleep(1)

print("Times up")
