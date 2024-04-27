

def is_leap(input_year):
    if input_year % 4 == 0:
        if input_year % 100 == 0:
            if input_year % 400 == 0:
                isLeap = True
            else:
                isLeap = False

        else:
            isLeap = True
    else:
        isLeap = False
    return isLeap


# TODO: Add more code here 👇
def days_in_month(input_year, input_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if input_month == 2 and is_leap(input_year):
        return 29
    else:
        return month_days[input_month - 1]

# Enter a year
year = int(input())
# Enter a month
month = int(input())
days = days_in_month(year, month)
print(days)
