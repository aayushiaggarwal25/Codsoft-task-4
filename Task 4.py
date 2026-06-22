
import random

CHOICES = ["rock", "paper", "scissors"]


def get_user_choice():
    """Keep asking until the user types a valid choice."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please type rock, paper, or scissors.")


def get_computer_choice():
    return random.choice(CHOICES)


def decide_winner(user_choice, computer_choice):
    """Returns 'user', 'computer', or 'tie' based on game rules."""
    if user_choice == computer_choice:
        return "tie"

    # All the ways the user can win
    user_wins = (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    )

    if user_wins:
        return "user"
    else:
        return "computer"


def play_round():
    print("\n--- New Round ---")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = decide_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

    return result


def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("Rock beats scissors, scissors beat paper, paper beats rock.\n")

    user_score = 0
    computer_score = 0

    while True:
        result = play_round()

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            break

    print("\nFinal Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations, you won overall!")
    elif user_score < computer_score:
        print("The computer won overall. Better luck next time!")
    else:
        print("Overall, it's a tie!")

    print("\nThanks for playing!")


# This makes sure the program runs only when this file is executed directly
if __name__ == "__main__":
    main()