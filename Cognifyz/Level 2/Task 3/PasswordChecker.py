import re

def check_password_strength(password):
    # Define regex patterns for different password requirements
    length_pattern = r".{8,}"  # At least 8 characters
    uppercase_pattern = r"[A-Z]"
    lowercase_pattern = r"[a-z]"
    digit_pattern = r"\d"
    special_character_pattern = r"[\W_]"  # Matches any non-alphanumeric character
    
    # Check each requirement and assign a score
    requirements = [
        (length_pattern, 2),
        (uppercase_pattern, 2),
        (lowercase_pattern, 2),
        (digit_pattern, 2),
        (special_character_pattern, 2)
    ]
    
    score = 0
    for pattern, points in requirements:
        if re.search(pattern, password):
            score += points
    
    return score

def main():
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    
    if strength >= 8:
        print("Password is strong!")
    elif strength >= 5:
        print("Password is moderate.")
    else:
        print("Password is weak.")

if __name__ == "__main__":
    main()
