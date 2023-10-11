import random

def get_user_choice():
    print("\nEnter your choice: rock, paper, or scissors.")
    user_choice = input().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    if (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return "user"
    return "computer"


user_score = 0
computer_score = 0

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "user":
        print("\nYou win!")
        user_score += 1
    elif winner == "computer":
        print("\nComputer wins!")
        computer_score += 1
    else:
        print("\nIt's a tie!")

    print(f"Score: User = {user_score} , Computer = {computer_score}")
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Final Score:")
        print(f"User - {user_score} | Computer - {computer_score}")
        break
