import random
from datetime import datetime
import os

def main():
    """
    Main program loop that handles the name shuffling process.
    
    The function manages the number of shuffle iterations and handles user input
    for continuing or ending the program. It will perform the specified number
    of shuffles and then ask the user if they want to continue.
    """
    count = 0
    NUM_SHUFFLES = 5  # Constants should be in uppercase
    
    # Create output directory if it doesn't exist
    output_dir = "shuffled_results"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    while count < NUM_SHUFFLES:
        # Generate unique filename for each shuffle
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{output_dir}/shuffled_names_{timestamp}.txt"
        
        shuffled_names = prompt_user()
        save_results(shuffled_names, output_filename, count + 1)
        count += 1
    
    print(f"\nAll results have been saved in the '{output_dir}' directory.")
    print("Want to start again? Type 'yes', if no, type 'nah'")
    response = input("Enter response: ").lower()
    
    if response == "yes":
        main()
    elif response == "nah":
        print("Have a nice day!")
    else:
        print("Error: Invalid input")
        quit()

def prompt_user():
    """
    Reads names from a file, shuffles them, and outputs a subset of unique names.
    
    The function performs the following steps:
    1. Opens and reads names from a file called "Names"
    2. Shuffles the names randomly
    3. Creates a list of unique names
    4. Outputs the first 5 unique names
    
    Returns:
        list: A list containing the selected shuffled names
    
    Note:
        - Expects a file named "Names" in the same directory
        - Each name in the file should be on a new line
        - Removes newline characters from the names before output
    """
    try:
        with open("Names.txt", "r+") as file:
            # Read all names from file
            names = file.readlines()
            
            # Shuffle the names randomly
            random.shuffle(names)
            
            # Create list of unique names, removing newline characters
            unique_names = []
            [unique_names.append(name.strip()) for name in names if name.strip() not in unique_names]
            
            # Get first 5 names
            selected_names = unique_names[:5]
            
            # Print the resulting list
            print(selected_names)
            
            return selected_names
            
    except FileNotFoundError:
        print("Error: 'Names' file not found in current directory")
        quit()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        quit()

def save_results(names, filename, shuffle_number):
    """
    Saves the shuffled names to a text file with additional metadata.
    
    Args:
        names (list): List of shuffled names to save
        filename (str): Path to the output file
        shuffle_number (int): Current shuffle iteration number
    
    The output file includes:
    - Timestamp of when the shuffle was performed
    - Shuffle iteration number
    - List of shuffled names
    """
    try:
        with open(filename, 'w') as f:
            f.write(f"Shuffle performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Shuffle iteration: {shuffle_number}\n")
            f.write("\nShuffled names:\n")
            for i, name in enumerate(names, 1):
                f.write(f"{i}. {name}\n")
        
        print(f"\nResults saved to: {filename}")
            
    except Exception as e:
        print(f"Error saving results to file: {str(e)}")

if __name__ == '__main__':
    main()