import random

def get_computer_choice():
    #Generate a random choice for the computer.
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    #Determine the winner based on user's choice and computer's choice.
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    """Main function to play the game."""
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Instructions: Choose rock, paper, or scissors to play.")
    print("Type 'exit' to end the game at any time.")
    
    while True:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        
        if user_choice == 'exit':
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if result == 'tie':
            print("It's a tie!")
        elif result == 'user':
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"\nCurrent Scores:\nYou: {user_score}\nComputer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("\nThanks for playing! Final Scores:")
    print(f"You: {user_score}\nComputer: {computer_score}")

if __name__ == "__main__":
    play_game()
