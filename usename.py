username = input("Enter your username: ")

space = username.find(" ")


if len(username) > 12:
    print("Your username cannot be more than 12 characters")
elif not space == -1:
    print("Your username cannot have any spaces")
elif not username.isalpha() == True:
    print("Your username cannot have any digit")
else:
    print(f"Welcome {username}")






