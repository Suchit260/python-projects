decision = input("Do you want to convert lbs to kgs or kgs to lbs? ")

if decision == "kgs to lbs":
    weight_in_kgs = float(input("Please enter your weight: "))
    weight_in_lbs = weight_in_kgs * 2.205
    print(f"Your weight in lbs is: {round(weight_in_lbs, 1)} lbs")
elif decision == "lbs to kgs":
    lbs = float(input("Please enter your weight: "))
    kgs = lbs/2.205
    print(f"Your weight in kgs is: {round(kgs, 1)} kgs")
else:
    print("Invalid input")
