name = input("What is your name?")
print("Hello " + name + " welcome to the game")

print("Its a guessing game which tests your general knowledge.")
start = input("Type start: ")
if start == "start" or start == "Start":
    q1 = input("1. Which country has the world's largest proven reserves of lithium, a critical component for electric vehicle batteries?  (A) Chile (B) China (C) Bolivia (D) Australia         ")
    q2 = input("2. The ancient city of Persepolis was the ceremonial capital of which empire? (A) Roman Empire (B) Achaemenid Empire (C) Ottoman Empire (D) Macedonian Empire                    ")
    q3 = input("3. What is the name of the first artificial satellite to orbit the Earth, and which country launched it? (A) Explorer 1 – USA   (B) Vostok 1 – Soviet Union   (C) Sputnik 1 – Soviet Union   (D) Luna 2 – Soviet Union               ")
    if q1 == "c" and q2 == "b" and q3 == "c" or q1 == "C" and q2 == "B" and q3 == "C":
        print("You win!")
    else:
        print("You lose!")
else:
    print("Okay then get out!")
