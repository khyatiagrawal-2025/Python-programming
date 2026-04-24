from datetime import *

# Accept date, month and year from the keyboard
d, m, y = [int(x) for x in input("Enter a date (dd/mm/yyyy): ").split('/')]

dt = date(y, m, d)

# %w - day number and %A full name of the week day
print(dt.strftime("Day %w of the week. This is %A"))