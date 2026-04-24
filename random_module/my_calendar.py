#To display calendar for entire year
from calendar import*
#program1
year = int(input("Enter Year:"))
print(calendar(year))

#program2
#To display calendar of given month of the year

#ask for month and year
year = int(input("enter your year : "))
mm = int(input("enter your month : "))
#Display the calendar for that month
str = month(year,mm)
print(str)
