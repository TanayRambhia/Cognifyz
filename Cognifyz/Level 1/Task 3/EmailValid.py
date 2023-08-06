import re

def is_valid_email(email):
    # Basic format check using regular expression
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    return False

# Test the function
email_addresses = [
    "user@example.com",
    "user.name@example.co.uk",
    "invalid.email",
    "12345@example.com",
    "user@.com",
]

for email in email_addresses:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
