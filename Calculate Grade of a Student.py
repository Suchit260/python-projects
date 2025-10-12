sub1 = int(input("Enter the marks for the first subject: "))
sub2 = int(input("Enter the marks for the second subject: "))
sub3 = int(input("Enter the marks for the third subject: "))
sub4 = int(input("Enter the marks for the fourth subject: "))
sub5 = int(input("Enter the marks for the fifth subject: "))

tot = sub1 + sub2+ sub3 + sub4 + sub5

percent = tot/5

if percent >= 90:
    print("A")
elif percent >= 80 and percent <= 90:
    print("B")
elif percent >= 70 and percent <= 80:
    print("C")
elif percent >= 60 and percent <= 70:
    print("D")
elif percent >= 50 and percent <= 60:
    print("E")
elif percent >= 40 and percent <= 50:
    print("F")
    
