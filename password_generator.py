import random
import string

def generate_password(length):
    #Generate a random password of the specified length.
    if length < 4:
        raise ValueError("Password length should be at least 4 characters for complexity.")

    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the remaining length with random choices from all sets
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

def main():
    #Main function to prompt user for password length and generate the password.
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length for your password: "))
            if length < 4:
                print("Password length should be at least 4 characters for complexity.")
                continue

            password = generate_password(length)
            print(f"Generated Password: {password}")
            
            play_again = input("\nDo you want to generate another password? (yes/no): ").lower()
            if play_again != 'yes':
                break
        except ValueError:
            print("Please enter a valid number.")

    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()
