import random
import string

def generate_password(length: int) -> str:
    """Generate a random password of a given length."""
    # Define the pool of characters
    char_pool = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the pool is not empty
    if length < 1:
        raise ValueError("Password length must be at least 1 character.")
    
    # Generate a random password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

def main():
    # User instructions
    print("Welcome to the Secure Password Generator!")
    print("Follow the prompts to generate your secure passwords.")
    
    # Get user inputs
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password: "))
        
        if num_passwords < 1:
            print("The number of passwords must be at least 1.")
            return
        
        if password_length < 1:
            print("The password length must be at least 1.")
            return
        
        print("\nGenerating passwords...\n")
        
        # Generate and display the passwords
        for i in range(num_passwords):
            print(f"Password {i+1}: {generate_password(password_length)}")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers for the number of passwords and their length.")
    
    print("\nThank you for using the Secure Password Generator!")

if __name__ == "__main__":
    main()
