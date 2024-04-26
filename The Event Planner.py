#Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
audio_system = "microphones" if attendees > 50 else "no microphones"
print(audio_system)
food = input("Do you want vegetarian food?: (yes/no) ")
if food == "yes":
 print("Veggie Delight Caterers for youuu!")
else:
 print("Hey, Gourmet Meals Caterers for you!")