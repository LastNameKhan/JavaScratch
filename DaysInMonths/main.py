leap_year = False
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        leap_year = True
      else:
        leap_year = False
    else:
      leap_year = True
  else:
    leap_year = False
  
# TODO: Add more code here 👇
def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if leap_year == True:
    month_days[1] = 29
    return month_days[month -1]
  else:
    return month_days[month - 1]
  

  
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

