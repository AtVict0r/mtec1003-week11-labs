maximumFloors = 26
currentFloor = int(input("On what floor of the building is your office? "))

while currentFloor < 1 or currentFloor > maximumFloors:
    print("You entered:", currentFloor, "which is greater than", maximumFloors,
          "which is the maximum number of floors in this building. Try again.")
    currentFloor = int(input("On what floor of the building is your office? "))
print("Congratulations! You work on floor", currentFloor)