import random
import string

def generate_password(length=12):
    """
    Generate a random password with the specified length.
    
    The password includes uppercase, lowercase, digits, and special characters.
    """
    if length < 4:  
        return "Error: Password length must be at least 4 characters."
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars),
    ]

    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
