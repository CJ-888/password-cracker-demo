import itertools
import string
import time

# Function to attempt cracking the password
def password_cracker(target_password):
    charset = string.ascii_letters + string.digits  
    max_length = len(target_password)
    
    start_time = time.time()  # Record the start time
    attempts = 0  # Counter for attempts

    for length in range(1, max_length + 1):  
        for guess in itertools.product(charset, repeat=length): 
            attempts += 1  
            guess_password = ''.join(guess)  # Convert tuple to string
            
            if guess_password == target_password:  # Check if the guess matches
                total_time = time.time() - start_time  # Calculate total time taken
                
                print(f"\nPassword found: {guess_password}")
                print(f"Total attempts made: {attempts}")
                print(f"Total time taken: {total_time:.2f} seconds")
                return guess_password
    
    print("\nPassword not found.")
    print(f"Total attempts made: {attempts}")
    return None

# Main function to run the cracker
def main():
    try:
        target_password = input("Enter the target password to crack: ").strip() 
        if not target_password:  # Check if the input is valid
            print("Error: Password cannot be empty. Please provide a valid password.")
            return
        
        print("\nStarting password cracking...\n")
        password_cracker(target_password)  # Call the cracker function
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
