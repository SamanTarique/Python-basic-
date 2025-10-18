import random

def play_game():
    print("\n Welcome to Rock Paper Scissors! ")
    print("Choices: rock, paper, scissors")

    options = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice: ").lower()
    
    if user_choice not in options:
        print(" Invalid choice! Please choose rock, paper, or scissors.")
        return 0

    computer_choice = random.choice(options)
    print(f" Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print(" It's a draw!")
        return 0.5
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        return 1
    else:
        print(" You lose!")
        return 0


# ---------------------- GAME LOOP ----------------------
score = 0
rounds = int(input("How many rounds do you want to play? "))

for i in range(rounds):
    print(f"\n Round {i + 1} of {rounds}")
    score += play_game()

# ---------------------- RESULTS ----------------------
print("\n Game Over!")
print(f" Your total score: {score}/{rounds}")

if score == rounds:
    print("Perfect! You defeated the computer in every round!")
elif score >= rounds / 2:
    print("Good game! You did well.")
else:
    print(" Better luck next time!")
