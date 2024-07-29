import random

print("Rock...Paper...Scissor")

Loop=int(input("How many times would you like to play? "))



player=""
scoreUser=0
scorePlayer=0

for i in range(1,Loop+1):
    
    user=input("Please enter your choice: ")
    num=random.randint(1,3)

    if num == 1:
        player = "Rock"
        print("Player's choice: ", player)
    elif num == 2:
        player = "Paper"
        print("Player's choice: ", player)
    elif player == 3: 
        player = "Scissor"
        print("Player's choice: ", player)


    if player == "Rock" and user == "Paper":
        print("You're winner")
        scoreUser+1
    elif player == "Paper" and user == "Paper":
        print("No one is winner")
    elif player == "Scissor" and user == "Paper":
        print("Player is winner")
        scorePlayer+1
    elif player == "Rock" and user == "Rock": 
        print("No one is winner")
    elif player == "Paper" and user == "Rock": 
        print("Player is winner")
        scorePlayer+1
    elif player == "Scissor" and user == "Rock": 
        print("You're winner")
        scoreUser+1
    elif player == "Rock" and user == "Scissor": 
        print("Player is winner")
        scorePlayer+1
    elif player == "Paper" and user == "Scissor": 
        print("You're winner")
        scoreUser+1
    elif player == "Scissor" and user == "Scissor": 
        print("No one is winner")

if scoreUser > scorePlayer:
    print("In the end you're winner:")
elif scorePlayer > scoreUser:
    print("In the end player is winner")
else:
    print("In the end no one is winner")

print("Player's score is: {0} ", scorePlayer)
print("Your score is: ", scoreUser)

