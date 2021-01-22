# CMPT 120
# Chatbot 2 (T-shirt Greeter Bot)
# Author: Henry Yin
# Section: D200

# Greeting the User
print("Hi! I am the T-shirt Greeter Chatbot 2!")

# Ask the user for the name
name= input("Your first and last name(one space in between)?-->")

# Respond to the user using the user's initials.
name_list=name.split()
first=name_list[0][0]
last=name_list[1][0]

print("Welcome ",first.upper()+last.upper(),"!!!")

# Ask the user his/her age(assume the user types correctly)
age=int(input("Your age?-->"))

# Compare last name initial with "L", and compare age with 18.
if (last.upper()<"L"):
    if(last.upper()=="A" or last.upper()=="B"):
        message= "You should go to: Queue A or B"
    else:
        message="You should go to: Queue before L"
else:
    message="You should go to: Queue L or after"
if (age<=18):
    message= message+"(youth)"
else:
    message= message+"(adult)"
print(message)

# Calculation

import math
import random

# n results from: Adding the length of the first name,
# the length of the last name, and the age. Calculate the square
# root of this number. n is integer part of this value.
num1= age + len(name) - 1 # substract the empty string in variable name.
num2= math.sqrt(num1)
n=int(num2)

# Calculate a random number (call it ran) between 1 and n
ran=random.randint(1,n)

# Inform the user the intermediate values: the sum, square root, n and ran.
print("TRACE- The sum is:",num1,"- sq root is",num2,"- n is:",n,"- ran is:",ran)

# Inform the user a text. The text should have
# the first and second letter in the user’s name repeated ran times
#followed by the number ran and followed by two exclamation signs.
print("Your Tshirt will have the text: "+(first.upper()+name_list[0][1])*ran+str(ran)+"!!")

# Say goodbye to user
print("BYE!")
