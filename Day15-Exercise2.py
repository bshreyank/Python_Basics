#Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. 
# Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

# Exercise 2
current_time = time.localtime().tm_hour

if current_time < 12:
    greeting="Good Morning"
elif current_time <18:
    greeting="Good Afternoon"
else:
    greeting="Good Evening"

print(greeting)
