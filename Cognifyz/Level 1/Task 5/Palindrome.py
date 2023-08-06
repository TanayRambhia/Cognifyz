def is_palindrome(input_str):
    # Remove spaces and convert to lowercase for accurate comparison
    clean_str = input_str.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return clean_str == clean_str[::-1]

# Test the function
strings_to_check = [
    "madam",
    "racecar",
    "hello",
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw",
]

for string in strings_to_check:
    if is_palindrome(string):
        print(f'"{string}" is a palindrome.')
    else:
        print(f'"{string}" is not a palindrome.')
