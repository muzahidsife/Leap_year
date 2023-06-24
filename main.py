def leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Year: "))
if leapyear(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
