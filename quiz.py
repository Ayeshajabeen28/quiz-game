print("WELCOME TO MY COMPUTER QUIZ-GAME!")

playing = input("Do you want to play the game?  ")

if playing.lower() != "yes":
    quit()
print("OKAY! let's start playing :)")
score = 0
#if playing.lower() == "yes":
 #   print("OKAY! let's start playing :)")
#else:
    #print("Quit")
#score

Answer = input("What is python?  ")
if Answer.lower() == "it is a programming language":
    print("correct!")
else:
    print("oops-sorry-incorrect-answer!")
    score +=1

Answer = input("RAM stamds for ?  ")
if Answer.lower() == "random access memory":
    print("correct!")
else:
    print("oops-sorry-incorrect-answer!")
    score += 1
Answer = input("capital of telangana?  ")
if Answer.lower() == "hyderabad":
    print("correct!")
else:
    print("oops-sorry-incorrect-answer!")
    score += 1
Answer = input("what is the color of crow?  ")
if Answer.lower() == "black":
    print("correct!")
else:
    print("oops-sorry-incorrect-answer!")
    score += 1

print("you got " + str((score/4)*100) + "%." )
