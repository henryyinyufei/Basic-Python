# CMPT 120
# Chatbot 3 - Travel Agent
# Author: Henry Yin
# Section: D200

# Greeting the User
print("\nHi! I am your travel agent bot!")

# Ask the name
name=input("\nWhat is your name? -->")

# Respond the user
print("Nice to meet you,",name,"!")

# Inform the user the general traveling options
def options():
    print("\nNote:")
    print("You will be able to choose:")
    print("\t- where to go")
    print("\t- travel modality")
    print("\t- style of trip")
    print("\t- length of trip")
    print("\nPlease provide your choice as asked.")
    print("If I do not understand you, I will choose for you.")
    return
options()

# Ask destinations
print("\nWe offer trips to Antartica, Bahamas, Cartagena or Washington")
destination=input("Where Would you like to go? -->").capitalize().strip("!")

# Respond the user
import random
list_destination=["Antartica","Bahamas","Cartagena","Washington"]
if (destination in list_destination):
    print("Nice! You chose", destination)
else:
    destination=random.choice(list_destination)
    print("I did not understand. I chose",destination,"for you")

# Ask travel modality 1
print("\nWe offer trips via 1-plane, 2-cruise, 3-bus, 4-hiking")
modality_1=int(input("Your first travel modality? (indicate the number) -->"))

# Respond the user (first travel modality)
list_modality=["plane","cruise","bus","hiking"]
if (modality_1>=1 and modality_1<=4):
    print("Good, your first choice is",list_modality[modality_1-1]) 
else:
    modality_1=random.randint(1,4)
    print("That is not a valid modality. I chose", list_modality[modality_1-1],"for you")

# Ask travel modality 2
modality_2=int(input("\nYour second travel modality? (number, 0 if none) -->"))

# Respond the user (second travel modality)
if (modality_2==0): 
    print("I see that you do not want another travel modality")
elif (modality_2>=1 and modality_2<=4):
    print("Good, you also chose:",list_modality[modality_2-1])
else:
    modality_2=random.randint(1,4)    
    print("That is not a valid modality. I chose",list_modality[modality_2-1],"for you")

# Ask trip style
print("\nWe offer trips style: regular or deluxe")
if (modality_1==4 or modality_2==4):
    trips_style="regular"
    print("Since you will be hiking, the style can only be",trips_style)
else:
    trips_style=input("Which style do you prefer? -->").lower()
    list_style=["regular","deluxe"]
    if (trips_style in list_style):
        print("Nice! you chose:",trips_style)
    else:
        trips_style=random.choice(list_style)
        print("I did not understand. I chose",trips_style,"for you")

# Ask length of trip
length=int(input("\nHow many days would you like to travel? -->"))

# TRACE
print("\nTRACE - Intermediate calculations cost")

# modality cost
if (modality_1==1 or modality_1==2):
    cost1=400*length
else:
    cost1=200*length
if (modality_2==0):
    cost2=0
elif (modality_2==1 or modality_2==2):
    cost2=400*length    
else:
    cost2=200*length
cost=cost1+cost2
print("TRACE - travelling cost (for",length,"days) is:",cost)

# extra cost
if (trips_style in ["regular"]):
    extra1=0
else:
    extra1=1000
if (destination in ["Antartica","Bahamas","Cartagena"]):
    message="destination < 'K'"
    extra2=0
else:
    message="destination > 'K'"
    extra2=50
extra=extra1+extra2
print("TRACE - extras (",trips_style,"and",message,") cost is:",extra)

# tax
print("TRACE - len(name):",len(name))

import math
tax=0.1 * len(name)* math.pi
print("TRACE - tax 10% len(name)* math.pi:",tax)

# total cost
Total=cost+extra+int(tax)
print("\n*** Your cost is:",Total)

# conclusion
print("\n********************")
print("Your trip will be to:",destination)
print("Travelling via:",list_modality[modality_1-1])
if (modality_2!=0):
    print("also travelling via:", list_modality[modality_2-1])
print("with style:",trips_style)

# reservation code
n=3 + length%4
code1=destination[0:3]*n
code2=str(n)
code3=list_modality[modality_1-1][0:2]
if modality_2==0:
    code4="*"
else:
    code4=list_modality[modality_2-1][0:2]
code=code1+code2+code3+code4
if (len(code)%2!=0):
    code5="$$"
else:
    code5="$"
reservation_code=code+code5
print("And reservation code: ",reservation_code.upper())
print("\n********************")

# TRACE
print("\nTRACE - n: 3+ reminder days divided by 4 is: ", n)
print("TRACE - length of reservation code before $ is: ", len(code))

# Ask the user
decision=input("\nDo you think you will travel with us? -->").lower().strip("!")
yeses = ["yes", "y","of course","certainly", "certainly yes", "sure"]
noses = ["no", "n","no way", "of course not", "never"]

# Respond
if (decision in yeses):
    print("Great!! Glad to hear that!")
elif (decision in noses):
    print("Ohhh maybe next time")
else:
    print("I don't understand.")
    print("But i'll take that as yes :)")

# say goodbye
byes=["Bye!","Nice doing business with you!","Adios!"]
print(random.choice(byes))



