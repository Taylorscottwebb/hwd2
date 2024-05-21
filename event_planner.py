# 2. Quick Decisions: The Event Planner 🎉
# Objective:

# To practice the use of shorthand if statements in determining event-related decisions.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

# Buggy Code:

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)
# Task 2: Venue Selection

# Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" 
# based on the number of attendees.

# Task 3: Catering Choices

# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".


attendees = int(input("Enter number of attendees: "))
venue = "large hall" 
if attendees > 100 :
    print ("large hall")
else : print("conference room")

if attendees < 100 :
    print("you should use a projector")
else:
    print("you should use a audio system")

food_caterers = input("Would you like vegetarian food at your event?:yes or no  ")
if food_caterers == "yes":
    print("You should use Veggie Delight Caterers")
else:
    print("You should use Gourmet Meals Caterers")



    