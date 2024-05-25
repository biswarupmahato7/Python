def find_next_leap_year(current_year):
    while True:
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
            return current_year
        current_year += 1

year = int(input('Enter Year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f'{year} is not a leper')
    next_leap_year = find_next_leap_year(year)
    print(f"The next leap year after {year} is: {next_leap_year}")
