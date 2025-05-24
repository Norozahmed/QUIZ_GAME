print("Welcome to the Quiz Game!")

playing  = input("Do you want to play? (yes/no): ").lower()
if playing != "yes":
    print("Goodbye!")
    quit()

print("Great! Let's start the game.")

score = 0

answer = input("What is does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Central Processing Unit'.")


answer = input("what does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Graphics Processing Unit'.")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Random Access Memory'.")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Power Supply Unit'.")

answer = input("What does SSD stands for? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Solid State Drive'.")

answer = input("What does HDD stands for? ")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Hard Disk Drive'.")

answer = input("What does USB stands for? ")
if answer.lower() == "universal serial bus":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Universal Serial Bus'.")

answer = input("What does BIOS stands for? ")
if answer.lower() == "basic input output system":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Basic Input Output System'.")

answer = input("What does OS stands for? ")
if answer.lower() == "operating system":
    print("Correct!")
    score += 1
else:   
    print("Incorrect! The correct answer is 'Operating System'.")

answer = input("What does URL stands for? ")
if answer.lower() == "uniform resource locator":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Uniform Resource Locator'.")

answer = input("What does HTTP stands for? ")
if answer.lower() == "hypertext transfer protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Hypertext Transfer Protocol'.")

answer = input("What does HTTPS stands for? ")
if answer.lower() == "hypertext transfer protocol secure":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Hypertext Transfer Protocol Secure'.")

# now tells the user how many questions they got right

print("You got " + str(score) + " out of 12 questions correct!")
print("Your score is " + str((score / 12) * 100) + "%")
print("Thanks for playing the Quiz Game!")