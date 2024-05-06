place = input("Choose a place: forest or cave? ")
if input != "forest or cave": pass 
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    if action == "cross a river":
        print("You found a boat!")

if place == "cave":
    action = input("Will you light a torch? : yes or no?") 
    if action == "yes":
            print("You find a hidden treasure!")
    if action == "no":
        print("You have wandered into a goblin layer and have been captured!!")
    