print("Enter Your Age: ")
age = int(input())

if (age >= 7) and (age <= 100):
    if age < 18:
        print("You cannot drive a vehicle")
    elif (age >= 18) and (age <= 80):
        print("You are eligible to drive a vehicle")
    else:
        print("Sorry, but you are too old to drive")
elif age < 7:
    print("You are way too young to be looking for this !")
else:
    print("Entered age is not valid")
