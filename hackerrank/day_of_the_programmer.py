
def dayOfProgrammer(year):
    month_days=243
    def is_leap_year(year):
        if year%4 == 0:
            if year<1918 or year%400 == 0 or year%100!=0:
                return True
            return False
        return False
    if is_leap_year(year):
        month_days += 1

    date=256-month_days
    print(f"{date}.09.{year}")
    # special case for transition from the Julian to Gregorian calendar in russia
    if year == 1918:
        return '26.09.1918'
    return f"{date}.09.{year}"


dayOfProgrammer(year=1918)