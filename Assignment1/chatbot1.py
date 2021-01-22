#  CMPT 120
#  Chatbot1 
#  Author: Henry Yin
#  Section: D200


# greeting the User
print("hello dear user!!!")

# ask the user for a name     
name= input("Please type your name ==> ")

message= "Nice to meet you, " + name + "!!!"

# answer something including a message, with the name within the message

print(message)

# ask what your (the user's) favourite food is 
food= input(name + ", What is your favourite food ? ==> ")

# make a comment about the food
message= "Wow, i like " + food + " too !!!"
print(message)

# ask the user's age
age= input("How old are you now, " + name + " ? ==>")

# calculate the age after 10 years
plus10= int(age) + 10

# inform the user the age 10 years later
message= "Then, 10 years later you will be " + str(plus10) + " years old !!! "
print(message)

# say goodbye to the User
print("Goodbye, "+ name +" , it was nice talking to you !!!")
