#Not as accurate as possible, could add day and month...
import datetime
name = raw_input("What's your name? ")
age = int(raw_input("How old are you? "))
now = datetime.datetime.now()
year = int(now.year)
print(year - age + 100)