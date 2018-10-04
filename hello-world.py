#First go
print("Hello, World!")

message = "Hello, World!"
print(message)
#-------> print "Hello World!" is Python 2 syntax, use print("Hello World!") for Python 3


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

print("Meal price from yesterday was $" + str(total) + ".")
#----------> Python doesn't like pound signs and euro signs in strings but $ is fine???


#Codeacademy's Madlibs
story = "%s wrote this story on a %s line train to test Python strings. Python is better than %s but worse than %s -------> written by %s on %02d/%02d/%02d at %02d:%02d"

story_name = raw_input("Enter a name: ")
story_line = raw_input("Enter a tube line: ")
story_programme_one = raw_input("Enter a programme: ")
story_programme_two = raw_input("Enter another programme: ")

print story % (story_name, story_line, story_programme_one, story_programme_two, story_name, now.day, now.month, now.year, now.hour, now.minute)
