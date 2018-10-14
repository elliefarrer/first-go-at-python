#Codeacademy's Madlibs
from datetime import datetime

now = datetime.now()
print(now)

story = "%s wrote this story on a %s line train to test Python strings. Python is better than %s but worse than %s -------> written by %s on %02d/%02d/%02d at %02d:%02d"

story_name = raw_input("Enter a name: ")
story_line = raw_input("Enter a tube line: ")
story_programme_one = raw_input("Enter a programme: ")
story_programme_two = raw_input("Enter another programme: ")

print story % (story_name, story_line, story_programme_one, story_programme_two, story_name, now.day, now.month, now.year, now.hour, now.minute)
