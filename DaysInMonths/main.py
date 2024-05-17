def is_leap(year):
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
  
def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) == True:
    month_days[1] = 29
    return f"Your Selected Year is {year} which is a Leap Year and days in your selected month is {month_days[month - 1]}"
  else:
    return month_days[month - 1]
  

  
year = int(input("Please Enter the year: \n"))
month = int(input("Please Enter a month: \n"))
days = days_in_month(year, month)
print(days)

