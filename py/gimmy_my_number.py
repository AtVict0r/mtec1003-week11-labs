myNumber = int(input("Gimme a number greater than 100...: "))

while myNumber <= 100:
    print(userNum, "is not a number greater than 100, try again!")
    userNum = int(input("Gimme a number greater than 100...: "))

print("You got it! The number", userNum, "is greater than 100!")