place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    if action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")