#Task 1: Code Correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?") #Task 2: Setting the Scene
    if action == "light a torch":
        print("You found a treasure!")
    else:
        print("You are stucked")
else: #Task 3: Default Path
    pass