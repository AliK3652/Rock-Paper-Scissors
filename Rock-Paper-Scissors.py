import random 

comp_wins = 0
user_wins = 0
user_options = ["rock", "paper", "scissors"]

while True:
    user_inp = input("Rock, Paper, or Scissors. 'q' to Quit\n").lower()
    if user_inp == "q":
        break
    if user_inp not in user_options:
        continue

    random_number = random.randint(0,2)
    comp_inp = user_options[random_number]
    print("Computer chooses", comp_inp + "." )

    if user_inp == comp_inp:
        print("Tie!")
        continue

    if user_inp == "rock" and comp_inp == "scissors":
        print("User Wins!")
        user_wins += 1

    elif user_inp == "paper" and comp_inp == "rock":
        print("User Wins!")
        user_wins += 1

    elif user_inp == "scissors" and comp_inp == "paper":
        print("User Wins!")
        user_wins += 1

    else:
        print("Computer Wins")
        comp_wins += 1

print("User Wins: ", user_wins)
print("Computer Wins: ", comp_wins)