#Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
audio_system = "microphones" if attendees > 50 else "no microphones"
print(audio_system)
food = input("Do you want vegetarian food?: (yes/no) ")
caterers = "Vegie Delight" if food == "yes" else "Gourmet Meals" 
print(caterers)