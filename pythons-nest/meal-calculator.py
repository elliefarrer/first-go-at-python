#Codeacademy calculator
meal = 44.5
print("Initial meal price is", meal)
tax = 6.75/100
tip = 15.0/100

meal = meal + meal * tax
print("Meal price with tax is", meal)

total = meal + (meal * tip)
print("Total is", total)

#Strings and datetime
from datetime import datetime

now = datetime.now()
print(now)

current_date_and_time = "Now it is %02d/%02d/%04d %02d:%02d:%02d" % (now.day, now.month, now.year, now.hour, now.minute, now.second)

print(current_date_and_time)
print(len(current_date_and_time))
print(current_date_and_time.upper())

print("Meal price from yesterday was $" + str(round(total, 2)) + ".")
#----------> Python doesn't like pound signs and euro signs in strings but $ is fine???
