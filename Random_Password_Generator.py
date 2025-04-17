import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one lowercase, one uppercase, one number, and one special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Add random characters to reach the desired length
    password += random.choices(characters, k=length-4)
    
    # Shuffle the list to avoid predictable patterns
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

# Ask the user for the desired password length
length = int(input("Enter password length: "))

# Generate and print the password
print("Generated password: ", generate_password(length))