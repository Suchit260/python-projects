def is_leap_year(year):
  
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year_to_check = 2024
if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")


print(f"Is 2023 a leap year? {is_leap_year(2023)}") 
print(f"Is 1900 a leap year? {is_leap_year(1900)}") 
print(f"Is 2000 a leap year? {is_leap_year(2000)}") 