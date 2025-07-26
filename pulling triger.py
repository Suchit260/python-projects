import time

mag = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

while len(mag) > 1:
    time.sleep(1)
    pull = mag.pop()
    release = mag.pop()
    print(f"Pull: {pull}, Release: {release}")

# Handle the last leftover item if mag has one element
if mag:
    time.sleep(1)
    pull = mag.pop()
    print(f"Pull: {pull}, Release: None")

print("mag empty")
