print("Welcome to my math quiz")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    print("Okay, maybe next time!")
    quit()

print("Okay! Let's play : )")
score = 0

answer = input("What is the square root of 4?")
if answer.lower() == "2":
    print('Correct!')
    score += 1 
else:
    print('Incorrect!')

answer = input("What is the square root of 9?")
if answer.lower() == "3":
    print('Correct!')
    score += 1
else:
     print('Incorrect!')

answer = input("What is the square root of 81?")
if answer.lower() == "9":
     print('Correct!')
     score += 1
else:
     print('Incorrect!')

answer = input("What is 2x = 6")
if answer.lower() == "x = 3":
     print('Correct!')
     score += 1
else:
     print('Incorrect!')
    
print("You've got " + str(score) +  " questions correct!")
print("You've got " + str((score / 4) * 100) + "% ")

