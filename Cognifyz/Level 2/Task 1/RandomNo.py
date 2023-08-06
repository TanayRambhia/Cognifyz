import random

def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I've chosen a random number between 1 and 100.")
    
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
    guess_number()
