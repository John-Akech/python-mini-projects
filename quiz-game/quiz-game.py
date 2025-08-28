print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()
if playing != "yes":
    print("Okay! Maybe next time.")
    quit()

print("Okay! Let's play :)\n")
score = 0
total_questions = 4

# Question 1
print(f"Question 1 of {total_questions}:")
answer = input("In what year was Python first released? ").lower()
if answer == "1991":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is 1991.\n")

# Question 2
print(f"Question 2 of {total_questions}:")
answer = input("What does HTTP stand for? ").lower()
if answer == "hypertext transfer protocol":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Hypertext Transfer Protocol.\n")

# Question 3
print(f"Question 3 of {total_questions}:")
answer = input("What is SQL used for? ").lower()
if "database" in answer:
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is: Managing databases.\n")

# Question 4
print(f"Question 4 of {total_questions}:")
answer = input("What does AI stand for? ").lower()
if answer == "artificial intelligence":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is Artificial Intelligence.\n")

print("Quiz Completed!")
print("You got " + str(score) + " questions correct!")
print("You got " + str(score / total_questions * 100) + "% correct!")
print("Thanks for playing!")
