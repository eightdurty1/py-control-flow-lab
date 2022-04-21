# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

user_month = input('Enter the month of the season (Jan - Dec): ')
user_day = int(input('Enter the day of the month: '))
if user_month in ('Jan', 'Feb', 'Mar'):
  season = 'Winter'
elif user_month in ('Apr', 'May', 'Jun'):
  season = 'Spring'
elif user_month in ('Jul', 'Aug', 'Sep'):
  season = 'Summer'
else:
  season = 'Fall'
if user_month == 'Mar' and user_day > 19:
  season = 'Spring'
elif user_month == 'Jun' and user_day > 20:
  season = 'Summer'
elif user_month == 'Sep' and duser_day > 21:
  season = 'Fall'
elif user_month == 'Dec' and user_day > 20:
  season = 'Winter'
print(f'{user_month} {user_day} is in {season}')
