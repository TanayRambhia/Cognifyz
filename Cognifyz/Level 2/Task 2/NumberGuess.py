import random

def number_guessing_game(min_number, max_number):
    target_number = random.randint(min_number, max_number)
    attempts = 0
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {min_number} and {max_number}.")
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < target_number:
                print("Too low! Try a higher number.")
            elif user_guess > target_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts.")
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    min_range = 1
    max_range = 100
    number_guessing_game(min_range, max_range)
