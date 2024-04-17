# Create a program using maths and F-Strings that tells us how many days, weeks, months
# we have left if we live until 90 years old
# You have x days, y weeks, and z months left

print("--- LIFE IN WEEKS ---")
YEARS = 90
MONTHS_A_YEAR = 12
WEEKS_A_YEAR = 52
DAYS_A_YEAR = 365
year_user = int(input("Type your age: "))
years_left = YEARS - year_user
months_left = years_left * MONTHS_A_YEAR
weeks_left = years_left * WEEKS_A_YEAR
days_left = years_left * DAYS_A_YEAR

meesage = f'You have {days_left} days, {weeks_left} weeks and {months_left} months left'

print(meesage)
